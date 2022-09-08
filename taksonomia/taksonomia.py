import datetime as dti
import hashlib
import json
import pathlib

CHUNK_SIZE = 2 << 15
EMPTY_SHA512 = (
    'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce'
    '47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'
)
ENCODING = 'utf-8'
TS_FORMAT = '%Y-%m-%d %H:%M:%S.%f +00:00'


class Taxonomy:
    """Collector of topological and size information on files in a tree."""

    def __init__(self, root: pathlib.Path) -> None:
        """Construct a collector instance for root."""
        self.root = root
        self.tree = {'sha512': EMPTY_SHA512, 'count_folders': 0, 'count_files': 0, 'branches': {}, 'leaves': {}}
        self.shadow = {'sha512_hash': hashlib.sha512(), 'branches': {}}

    def branch(self, path: pathlib.Path) -> None:
        """Add a folder (sub tree) entry."""
        st = path.stat()
        branch = str(path)
        self.tree['branches'][branch] = {  # type: ignore
            'sha512': EMPTY_SHA512,
            'count_folders': 1,
            'count_files': 0,
            'size_bytes': 0,
            'mod_time': dti.datetime.fromtimestamp(st.st_ctime, tz=dti.timezone.utc).strftime(TS_FORMAT),
        }
        self.shadow['branches'][branch] = hashlib.sha512()  # type: ignore
        for parent in path.parents:
            branch = str(parent)
            if branch in self.tree['branches']:  # type: ignore
                self.tree['branches'][branch]['count_folders'] += 1  # type: ignore

    @staticmethod
    def hash_file(path: pathlib.Path) -> str:
        """Return the SHA512 hex digest of the data from file."""
        hash = hashlib.sha512()
        with open(path, 'rb') as handle:
            while chunk := handle.read(CHUNK_SIZE):
                hash.update(chunk)
        return hash.hexdigest()

    def leaf(self, path: pathlib.Path) -> None:
        """Add a folder (sub tree) entry."""
        st = path.stat()
        hash = self.hash_file(path)

        self.tree['leaves'][str(path)] = {  # type: ignore
            'sha512': hash,
            'count_folders': 0,
            'count_files': 1,
            'size_bytes': st.st_size,
            'mod_time': dti.datetime.fromtimestamp(st.st_ctime, tz=dti.timezone.utc).strftime(TS_FORMAT),
        }

        self.shadow['sha512_hash'].update(hash.encode(ENCODING))  # type: ignore
        self.tree['sha512'] = self.shadow['sha512_hash'].hexdigest()  # type: ignore
        for parent in path.parents:
            branch = str(parent)
            if branch in self.tree['branches']:  # type: ignore
                self.tree['branches'][branch]['count_files'] += 1  # type: ignore
                self.tree['branches'][branch]['size_bytes'] += st.st_size  # type: ignore
                self.shadow['branches'][branch].update(hash.encode(ENCODING))  # type: ignore
                self.tree['branches'][branch]['sha512'] = self.shadow['branches'][branch].hexdigest()  # type: ignore

    def __repr__(self) -> str:
        """Express yourself."""
        return json.dumps(self.tree, indent=2)


def parse():  # type: ignore
    return NotImplemented


def main(root: pathlib.Path) -> Taxonomy:
    """Visit the folder tree below root and return the taxonomy."""
    taxonomy = Taxonomy(root)
    for path in sorted(root.glob('**/')):
        taxonomy.branch(path)
    for path in sorted(root.rglob('*')):
        if path.is_file():
            taxonomy.leaf(path)
    return taxonomy
