"""Taxonomy (Finnish: taksonomia) guided by conventions of a folder tree (implementation)."""
import argparse
import datetime as dti
import hashlib
import json
import os
import pathlib
import platform
import sys
import uuid
from typing import no_type_check

import psutil  # type: ignore
from cpuinfo import get_cpu_info  # type: ignore

CHUNK_SIZE = 2 << 15
EMPTY_SHA512 = (
    'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce'
    '47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'
)
EMPTY_SHA256 = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
EMPTY = {
    'sha512': EMPTY_SHA512,
    'sha256': EMPTY_SHA256,
}
HASH_ALGO_PREFS = tuple(EMPTY)
ENCODING = 'utf-8'
TS_FORMAT = '%Y-%m-%d %H:%M:%S.%f +00:00'


@no_type_check
class Taxonomy:
    """Collector of topological and size information on files in a tree."""

    def __init__(self, root: pathlib.Path) -> None:
        """Construct a collector instance for root."""
        self.root = root
        self.hasher = {
            'sha512': hashlib.sha512,
            'sha256': hashlib.sha256,
        }
        self.pid = os.getpid()
        self.start_time = dti.datetime.now(tz=dti.timezone.utc)

        self.tree = {
            'hash_algo_prefs': list(HASH_ALGO_PREFS),
            'context': {
                'start_ts': self.start_time.strftime(TS_FORMAT),
                'end_ts': None,
                'duration_usecs': 0,
                **self.machine_context(path_selector=str(self.root)),  # type: ignore
                'pwd': str(pathlib.Path.cwd()),
                'tree_root': str(self.root),
                'machine_perf': {
                    'pre': self.machine_perf(self.pid),  # type: ignore
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
        self.shadow = {**{algo: self.hasher[algo]() for algo in HASH_ALGO_PREFS}, 'branches': {}}  # type: ignore

    @no_type_check
    def machine_perf(self, pid: int):
        """Some random information from machine performance measures."""
        p = psutil.Process(pid)
        cpts = p.cpu_times()
        cpts_union_attrs = ('children_system', 'children_user', 'system', 'user')
        mfi = p.memory_full_info()
        mfi_union_attrs = ('pageins', 'pfaults', 'rss', 'uss', 'vms')
        threads = p.threads()
        thr_union_attrs = ('id', 'system_time', 'user_time')
        ctxs = p.num_ctx_switches()
        ctxs_union_attrs = ('involuntary', 'voluntary')
        return {
            'name': p.name(),
            'status': p.status(),
            'create_time': dti.datetime.fromtimestamp(p.create_time(), dti.timezone.utc).strftime(TS_FORMAT),
            'username': p.username(),
            'cpu_times': {aspect: getattr(cpts, aspect, None) for aspect in cpts_union_attrs},
            'memory_full_info': {aspect: getattr(mfi, aspect, None) for aspect in mfi_union_attrs},
            'memory_percent': p.memory_percent(),
            'num_threads': p.num_threads(),
            'threads': [{aspect: getattr(thr, aspect, None) for aspect in thr_union_attrs} for thr in threads],
            'num_fds': p.num_fds(),
            'num_ctx_switches': {aspect: getattr(ctxs, aspect, None) for aspect in ctxs_union_attrs},
        }

    @no_type_check
    def machine_context(self, path_selector: str):
        """Some random information from machine context."""
        swa = psutil.swap_memory()
        swa_union_attrs = ('free', 'percent', 'sin', 'sout', 'total', 'used')
        vim = psutil.virtual_memory()
        vim_union_attrs = (
            'active',
            'available',
            'buffers',
            'cached',
            'free',
            'inactive',
            'percent',
            'shared',
            'slab',
            'total',
            'used',
            'wired',
        )
        dic = psutil.disk_io_counters(perdisk=False)
        dic_union_attrs = ('read_bytes', 'read_count', 'read_time', 'write_bytes', 'write_count', 'write_time')
        du = psutil.disk_usage(path_selector)
        du_union_attrs = ('free', 'percent', 'total', 'used')
        dpas = psutil.disk_partitions()
        dpa_union_attrs = ('device', 'fstype', 'maxfile', 'maxpath', 'mountpoint')
        partitions = []
        for dpa in dpas:
            partitions.append(
                {
                    **{aspect: getattr(dpa, aspect, None) for aspect in dpa_union_attrs},
                    'opts': dpa.opts.split(',') if hasattr(dpa, 'opts') else None,
                }
            )

        return {
            'node_identifier': str(uuid.uuid3(uuid.NAMESPACE_DNS, platform.node())),
            'pid': os.getpid(),
            'ppid': os.getppid(),
            'boottime': dti.datetime.fromtimestamp(psutil.boot_time(), dti.timezone.utc).strftime(TS_FORMAT),
            'cpu_info': {**get_cpu_info()},
            'memory': {
                'swap': {aspect: getattr(swa, aspect, None) for aspect in swa_union_attrs},
                'virtual': {aspect: getattr(vim, aspect, None) for aspect in vim_union_attrs},
            },
            'disks': {
                'counters_combined': {aspect: getattr(dic, aspect, None) for aspect in dic_union_attrs},
                'partitions': partitions,
                'path_selector': path_selector,
                'usage': {aspect: getattr(du, aspect, None) for aspect in du_union_attrs},
            },
        }

    def branch(self, path: pathlib.Path) -> None:
        """Add a folder (sub tree) entry."""
        st = path.stat()
        branch = str(path)
        self.tree['branches'][branch] = {  # type: ignore
            'hash_hexdigest': {**{algo: self.hasher[algo]() for algo in HASH_ALGO_PREFS}},
            'summary': {
                'count_branches': 1,
                'count_leaves': 0,
                'size_bytes': 0,
            },
            'mod_time': dti.datetime.fromtimestamp(st.st_ctime, tz=dti.timezone.utc).strftime(TS_FORMAT),
        }
        self.shadow['branches'][branch] = {**{algo: self.hasher[algo]() for algo in HASH_ALGO_PREFS}}
        self.tree['summary']['count_branches'] += 1  # type: ignore
        for parent in path.parents:
            branch = str(parent)
            if branch in self.tree['branches']:
                self.tree['branches'][branch]['summary']['count_branches'] += 1  # type: ignore

    def hash_file(self, path: pathlib.Path, algo: str = 'sha512') -> str:
        """Return the SHA512 hex digest of the data from file."""
        if algo not in self.hasher:
            raise KeyError(f'Unsupported hash algorithm requested - {algo} is not in ({HASH_ALGO_PREFS})')

        hash = self.hasher[algo]()
        with open(path, 'rb') as handle:
            while chunk := handle.read(CHUNK_SIZE):
                hash.update(chunk)
        return hash.hexdigest()

    def leaf(self, path: pathlib.Path) -> None:
        """Add a folder (sub tree) entry."""
        st = path.stat()
        size_bytes = st.st_size
        mod_time = dti.datetime.fromtimestamp(st.st_ctime, tz=dti.timezone.utc).strftime(TS_FORMAT)
        leaf = str(path)
        self.tree['leaves'][leaf] = {  # type: ignore
            'hash_hexdigest': {algo: self.hash_file(path, algo) for algo in HASH_ALGO_PREFS},
            'size_bytes': size_bytes,
            'mod_time': mod_time,
        }

        hexdig = 'hash_hexdigest'
        for algo in HASH_ALGO_PREFS:
            self.shadow[algo].update(self.tree['leaves'][leaf][hexdig][algo].encode(ENCODING))  # type: ignore
            self.tree['summary'][hexdig][algo] = self.shadow[algo].hexdigest()  # type: ignore
        self.tree['summary']['size_bytes'] += size_bytes  # type: ignore
        self.tree['summary']['count_leaves'] += 1  # type: ignore
        for parent in path.parents:
            b = str(parent)
            if b in self.tree['branches']:
                self.tree['branches'][b]['summary']['count_leaves'] += 1  # type: ignore
                self.tree['branches'][b]['summary']['size_bytes'] += size_bytes  # type: ignore
                shadow_sum = self.shadow['branches'][b]
                for algo in HASH_ALGO_PREFS:
                    shadow_sum[algo].update(self.tree['leaves'][leaf][hexdig][algo].encode(ENCODING))  # type: ignore
                    self.tree['branches'][b][hexdig][algo] = shadow_sum[algo].hexdigest()  # type: ignore

    @no_type_check
    def report(self):
        """Create the post visitation machine context perf entry and report the taxaonomy."""
        self.tree['context']['machine_perf']['post'] = self.machine_perf(self.pid)
        end_time = dti.datetime.now(tz=dti.timezone.utc)
        self.tree['context']['end_ts'] = end_time.strftime(TS_FORMAT)
        self.tree['context']['duration_usecs'] = (end_time - self.start_time).microseconds
        return self.tree

    def __repr__(self) -> str:
        """Express yourself."""
        return json.dumps(self.tree, indent=2)


def parse():  # type: ignore
    return NotImplemented


def main(options: argparse.Namespace) -> int:
    """Visit the folder tree below root and return the taxonomy."""
    tree_root = pathlib.Path(options.tree_root)

    visit = Taxonomy(tree_root)
    for path in sorted(tree_root.rglob('*')):
        if path.is_dir():
            visit.branch(path)
        elif path.is_file():
            visit.leaf(path)
        else:
            raise ValueError(f'path ({path}) is neither a folder nor a file')

    taxonomy = visit.report()

    if options.out_path is sys.stdout:
        print(json.dumps(taxonomy, indent=2))
        return 0

    out_path = pathlib.Path(options.out_path)
    with open(out_path, 'wt', encoding=ENCODING) as handle:
        json.dump(taxonomy, handle, indent=2)

    return 0
