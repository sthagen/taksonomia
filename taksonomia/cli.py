"""CLI operations for taxonomy (Finnish: taksonomia) guided by conventions of a folder tree.."""
import argparse
import sys
from typing import List, Union

import taksonomia.taksonomia as api
from taksonomia import APP_ALIAS


def parse_request(argv: List[str]) -> argparse.Namespace:
    """DRY."""
    parser = argparse.ArgumentParser(description=APP_ALIAS)
    parser.add_argument(
        '--tree-root',
        '-t',
        dest='tree_root',
        help='tree root',
        required=True,
    )
    parser.add_argument(
        '--out-path',
        '-o',
        dest='out_path',
        default='taxonomy.json',
        help=(f'output file path for taxonomy (default: {APP_ALIAS}.json)'),
    )
    return parser.parse_args(argv)


# pylint: disable=expression-not-assigned
def main(argv: Union[List[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    options = parse_request(argv)
    return api.main(options)
