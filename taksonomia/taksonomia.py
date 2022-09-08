import datetime as dti
import hashlib
import json
import logging
import pathlib
from typing_extensions import Self

import orjson

CHUNK_SIZE = 2 << 15
EMPTY_SHA512 = (
    'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce'
    '47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'
)
TS_FORMAT = '%Y-%m-%d %H:%M:%S.%f +00:00'
class Taxonomy:
    """Collector of topological and size information on files in a tree."""
    def __init__(self, root: pathlib.Path) -> Self:
        """Construct a collector instance for root."""
        self.root = root
        self.tree = {
            'sha512' : EMPTY_SHA512,
            'count_folders': 0,
            'count_files': 0,
            'branches': {

            },
            'leaves': {

            }
        }

    def branch(self, path: pathlib.Path) -> None:
        """Add a folder (sub tree) entry."""
        st = path.stat()

        self.tree['branches'][str(path)] = {
            'sha512' : EMPTY_SHA512,
            'count_folders': 1,
            'count_files': 0,
            'size_bytes': 0,
            'mod_time': dti.datetime.fromtimestamp(st.st_ctime, tz=dti.timezone.utc).strftime(TS_FORMAT),
        }
        for parent in path.parents:
            branch = str(parent)
            if branch in self.tree['branches']:
                self.tree['branches'][branch]['count_folders'] += 1

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

        self.tree['leaves'][str(path)] = {
            'sha512' : hash,
            'count_folders': 0,
            'count_files': 1,
            'size_bytes': st.st_size,
            'mod_time': dti.datetime.fromtimestamp(st.st_ctime, tz=dti.timezone.utc).strftime(TS_FORMAT),
        }

        for parent in path.parents:
            branch = str(parent)
            if branch in self.tree['branches']:
                self.tree['branches'][branch]['count_files'] += 1
                self.tree['branches'][branch]['size_bytes'] += st.st_size

    def __repr__(self):
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
    print(taxonomy)
    return taxonomy
