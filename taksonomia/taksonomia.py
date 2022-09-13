"""Taxonomy (Finnish: taksonomia) of a folder tree, guided by conventions. (implementation)."""
import argparse
import base64
import datetime as dti
import hashlib
import lzma
import os
import pathlib
import sys
from typing import no_type_check

import orjson
import yaml

import taksonomia.anglify as anglify
from taksonomia import (
    APP_ALIAS,
    COMMA,
    ENCODING,
    KNOWN_FORMATS,
    KNOWN_KEY_FUNCTIONS,
    TS_FORMAT,
    __version_info__ as VERSION_INFO,
    log,
)
from taksonomia.machine import Machine

CHUNK_SIZE = 2 << 15
DOCTYPE = '<?xml version="1.0" encoding="UTF-8"?>'
EMPTY_SHA256 = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
EMPTY_SHA512 = (
    'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce'
    '47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'
)
EMPTY = {
    'sha512': EMPTY_SHA512,
    'sha256': EMPTY_SHA256,
}
ENCODING_ERRORS_POLICY = 'ignore'
HASH_ALGO_PREFS = tuple(EMPTY)
ORJSON_OPTIONS = orjson.OPT_INDENT_2 | orjson.OPT_APPEND_NEWLINE
TAX = 'taxonomy'
XMLNS = 'https://pypi.org/project/taksonomia/api/v1'
XZ_EXT = '.xz'
XZ_FILTERS = [{'id': lzma.FILTER_LZMA2, 'preset': 7 | lzma.PRESET_EXTREME}]


def elf_hash(some_bytes: bytes) -> int:
    """The ELF hash (Extremely Lossy Function - also used in ELF format).
    unsigned long ElfHash(const unsigned char *s) {
        unsigned long h = 0, high;
        while (*s) {
            h = (h << 4) + *s++;
            if (high = h & 0xF0000000)
                h ^= high >> 24;
            h &= ~high;
        }
        return h;
    }
    """
    h = 0
    for s in some_bytes:
        h = (h << 4) + s
        high = h & 0xF0000000
        if high:
            h ^= high >> 24
        h &= ~high
    return h


@no_type_check
class Taxonomy:
    """Collector of topological and size information on files in a tree."""

    def __init__(self, root: pathlib.Path, excludes: str, key_function: str = 'elf') -> None:
        """Construct a collector instance for root."""
        self.root = root
        self.excludes = sorted(part.strip() for part in excludes.split(COMMA) if part.strip())
        self.key_function = key_function.lower()
        if self.key_function not in KNOWN_KEY_FUNCTIONS:
            raise ValueError(f'key function {key_function} not in {KNOWN_KEY_FUNCTIONS}')

        self.perspective = str(pathlib.Path.cwd())
        self.closed = False
        self.hasher = {
            'sha512': hashlib.sha512,
            'sha256': hashlib.sha256,
        }
        self.pid = os.getpid()
        self.machine = Machine(str(self.root), self.pid)
        self.start_time = dti.datetime.now(tz=dti.timezone.utc)

        self.tree = {
            TAX: {
                'hash_algo_prefs': list(HASH_ALGO_PREFS),
                'key_function': self.key_function,
                'generator': {
                    'name': APP_ALIAS,
                    'version_info': list(VERSION_INFO),
                    'source': f'https://pypi.or/project/taksonomia/{".".join(VERSION_INFO[:3])}/',
                    'sbom': 'https://codes.dilettant.life/docs/taksonomia/third-party/',
                },
                'context': {
                    'start_ts': self.start_time.strftime(TS_FORMAT),
                    'end_ts': None,
                    'duration_usecs': 0,
                    **self.machine.context(),
                    'pwd': self.perspective,
                    'tree_root': str(self.root),
                    'excludes': self.excludes,
                    'machine_perf': {
                        'pre': self.machine.perf(),
                        'post': None,
                    },
                },
                'summary': {
                    'hash_hexdigest': {**{algo: EMPTY[algo] for algo in HASH_ALGO_PREFS}},
                    'count_branches': 0,
                    'count_leaves': 0,
                    'size_bytes': 0,
                },
                'branches': {},
                'leaves': {},
            }
        }
        self.shadow = {**{algo: self.hasher[algo]() for algo in HASH_ALGO_PREFS}, 'branches': {}}  # type: ignore

    def ignore(self, path: pathlib.Path) -> bool:
        """Dry place for the filter hook (excludes)."""
        text = str(path)
        return bool(self.excludes) and any(exclude in text for exclude in self.excludes)

    def key(self, path_str: str) -> str:
        """Hashing function for the path keys."""
        if self.key_function == 'elf':
            return str(elf_hash(path_str.encode(ENCODING)))
        return hashlib.md5(path_str.encode(ENCODING)).hexdigest()  # nosec B324

    def add_branch(self, path: pathlib.Path) -> None:
        """Add a folder (sub tree) entry."""
        if self.ignore(path):
            return

        st = path.stat()
        branch = str(path)
        self.tree[TAX]['branches'][self.key(branch)] = {  # type: ignore
            'path': branch,
            'hash_hexdigest': {**{algo: EMPTY[algo] for algo in HASH_ALGO_PREFS}},
            'summary': {
                'count_branches': 1,
                'count_leaves': 0,
                'size_bytes': 0,
            },
            'mod_time': dti.datetime.fromtimestamp(st.st_ctime, tz=dti.timezone.utc).strftime(TS_FORMAT),
        }
        self.shadow['branches'][self.key(branch)] = {**{algo: self.hasher[algo]() for algo in HASH_ALGO_PREFS}}
        self.tree[TAX]['summary']['count_branches'] += 1  # type: ignore
        for parent in path.parents:
            branch_key = self.key(str(parent))
            if branch_key in self.tree[TAX]['branches']:
                self.tree[TAX]['branches'][branch_key]['summary']['count_branches'] += 1  # type: ignore

    def hash_file(self, path: pathlib.Path, algo: str = 'sha512') -> str:
        """Return the SHA512 hex digest of the data from file."""
        if algo not in self.hasher:
            raise KeyError(f'Unsupported hash algorithm requested - {algo} is not in {HASH_ALGO_PREFS}')

        hash = self.hasher[algo]()
        with open(path, 'rb') as handle:
            while chunk := handle.read(CHUNK_SIZE):
                hash.update(chunk)
        return hash.hexdigest()

    def add_leaf(self, path: pathlib.Path) -> None:
        """Add a folder (sub tree) entry."""
        if self.ignore(path):
            return

        st = path.stat()
        size_bytes = st.st_size
        mod_time = dti.datetime.fromtimestamp(st.st_ctime, tz=dti.timezone.utc).strftime(TS_FORMAT)
        leaf = str(path)
        self.tree[TAX]['leaves'][self.key(leaf)] = {  # type: ignore
            'path': leaf,
            'hash_hexdigest': {algo: self.hash_file(path, algo) for algo in HASH_ALGO_PREFS},
            'size_bytes': size_bytes,
            'mod_time': mod_time,
        }

        hexdig = 'hash_hexdigest'
        for algo in HASH_ALGO_PREFS:
            self.shadow[algo].update(
                self.tree[TAX]['leaves'][self.key(leaf)][hexdig][algo].encode(ENCODING)  # type: ignore
            )
            self.tree[TAX]['summary'][hexdig][algo] = self.shadow[algo].hexdigest()  # type: ignore
        self.tree[TAX]['summary']['size_bytes'] += size_bytes  # type: ignore
        self.tree[TAX]['summary']['count_leaves'] += 1  # type: ignore
        for parent in path.parents:
            bk = self.key(str(parent))
            if bk in self.tree[TAX]['branches']:
                self.tree[TAX]['branches'][bk]['summary']['count_leaves'] += 1  # type: ignore
                self.tree[TAX]['branches'][bk]['summary']['size_bytes'] += size_bytes  # type: ignore
                shadow_sum = self.shadow['branches'][bk]
                for algo in HASH_ALGO_PREFS:
                    shadow_sum[algo].update(
                        self.tree[TAX]['leaves'][self.key(leaf)][hexdig][algo].encode(ENCODING)  # type: ignore
                    )
                    self.tree[TAX]['branches'][bk][hexdig][algo] = shadow_sum[algo].hexdigest()  # type: ignore

    def close(self) -> None:
        """Create the post visitation machine context perf entry (if needed))."""
        if not self.closed:
            self.tree[TAX]['context']['machine_perf']['post'] = self.machine.perf()  # type: ignore
            end_time = dti.datetime.now(tz=dti.timezone.utc)
            self.tree[TAX]['context']['end_ts'] = end_time.strftime(TS_FORMAT)  # type: ignore
            self.tree[TAX]['context']['duration_usecs'] = (end_time - self.start_time).microseconds  # type: ignore
            self.closed = True

    @no_type_check
    def report(self):
        """Create the post visitation machine context perf entry (if needed) and report the taxonomy."""
        self.close()
        return self.tree

    def __repr__(self) -> str:
        """Express yourself."""
        return orjson.dumps(self.tree, option=ORJSON_OPTIONS).decode(encoding=ENCODING)

    @no_type_check
    def json_to(self, sink: object, base64_encode: bool = False, xz_compress: bool = False) -> None:
        """Close the taxonomy collection and write tree in json format to sink."""
        self.close()
        if sink is sys.stdout:
            if xz_compress:
                log.warning('ignoring --xz-compress for now as json output goes to std out')
            if base64_encode:
                print(base64.b64encode(orjson.dumps(self.tree, option=ORJSON_OPTIONS)).decode(encoding=ENCODING))
                return
            print(orjson.dumps(self.tree, option=ORJSON_OPTIONS).decode(encoding=ENCODING))
            return

        if xz_compress:
            with lzma.open(pathlib.Path(sink), 'wb', check=lzma.CHECK_SHA256, filters=XZ_FILTERS) as handle:
                handle.write(orjson.dumps(self.tree, option=ORJSON_OPTIONS))
            return

        with open(pathlib.Path(sink), 'wb') as handle:
            if base64_encode:
                handle.write(base64.b64encode(orjson.dumps(self.tree, option=ORJSON_OPTIONS)))
            else:
                handle.write(orjson.dumps(self.tree, option=ORJSON_OPTIONS))

    @no_type_check
    def xml_to(self, sink: object, base64_encode: bool = False, xz_compress: bool = False) -> None:
        """Close the taxonomy collection and write tree in xml format to sink."""
        self.close()
        xml_str = anglify.as_xml(self.tree)
        if sink is sys.stdout:
            if xz_compress:
                log.warning('ignoring --xz-compress for now as xml output goes to std out')
            if base64_encode:
                print(str(base64.b64encode(xml_str.encode(encoding=ENCODING)).decode(encoding=ENCODING)))
                return
            print(xml_str)
            return

        if xz_compress:
            with lzma.open(pathlib.Path(sink), 'w', check=lzma.CHECK_SHA256, filters=XZ_FILTERS) as handle:
                handle.write(xml_str.encode(encoding=ENCODING, errors=ENCODING_ERRORS_POLICY))
            return

        with open(pathlib.Path(sink), 'wt', encoding=ENCODING) as handle:
            if base64_encode:
                handle.write(base64.b64encode(xml_str.encode(encoding=ENCODING)).decode(encoding=ENCODING))
            else:
                handle.write(xml_str)

    @no_type_check
    def yaml_to(self, sink: object, base64_encode: bool = False, xz_compress: bool = False) -> None:
        """Close the taxonomy collection and write tree in yaml format to sink."""
        self.close()
        if sink is sys.stdout:
            if xz_compress:
                log.warning('ignoring --xz-compress for now as yaml output goes to std out')
            if base64_encode:
                print(str(base64.b64encode(yaml.dump(self.tree).encode(encoding=ENCODING)).decode(encoding=ENCODING)))
                return
            print(yaml.dump(self.tree))
            return

        if xz_compress:
            with lzma.open(pathlib.Path(sink), 'w', check=lzma.CHECK_SHA256, filters=XZ_FILTERS) as handle:
                handle.write(yaml.dump(self.tree).encode(encoding=ENCODING, errors=ENCODING_ERRORS_POLICY))
            return

        with open(pathlib.Path(sink), 'wt', encoding=ENCODING) as handle:
            if base64_encode:
                handle.write(base64.b64encode(yaml.dump(self.tree).encode(encoding=ENCODING)).decode(encoding=ENCODING))
            else:
                yaml.dump(self.tree, handle)

    @no_type_check
    def dump(self, sink: object, format_type: str, base64_encode: bool = False, xz_compress: bool = False) -> None:
        """Dump the assumed to be final taxonomy (tree) in json or yaml format."""
        if format_type.lower() not in KNOWN_FORMATS:
            raise ValueError(f'requested format {format_type} for taxonomy dump not in {KNOWN_FORMATS}')

        if format_type.lower() == 'json':
            return self.json_to(sink, base64_encode, xz_compress)
        if format_type.lower() == 'xml':
            return self.xml_to(sink, base64_encode, xz_compress)
        return self.yaml_to(sink, base64_encode, xz_compress)


def parse():  # type: ignore
    return NotImplemented


def main(options: argparse.Namespace) -> int:
    """Visit the folder tree below root and yield the taxonomy."""
    tree_root = pathlib.Path(options.tree_root)
    log.info(f'Assessing taxonomy of folder {tree_root}')
    log.info(f'Output channel is {"STDOUT" if options.out_path is sys.stdout else options.out_path}')
    if options.excludes.strip():
        exploded = tuple(options.excludes.strip().split(COMMA))
        log.info(f'Requested exclusion of ({", ".join(exploded)}) partial{"" if len(exploded) == 1 else "s"}')
    if options.xz_compress:
        log.info('Requested xz compression (LZMA)')
    if options.base64_encode:
        log.info('Requested encoding (BASE64)')
    taxonomy = Taxonomy(tree_root, options.excludes, options.key_function)
    for path in sorted(tree_root.rglob('*')):
        if path.is_dir():
            log.info(f'Detected branch {path}')
            taxonomy.add_branch(path)
            continue
        taxonomy.add_leaf(path)
        log.info(f'Detected leaf {path}')

    taxonomy.dump(
        sink=options.out_path,
        format_type=options.format_type,
        base64_encode=options.base64_encode,
        xz_compress=options.xz_compress,
    )
    duration_secs = taxonomy.tree['taxonomy']['context']['duration_usecs'] / 1.0e6  # type: ignore
    log.info(f'Assessed taxonomy of folder {tree_root} in {duration_secs} secs')

    return 0
