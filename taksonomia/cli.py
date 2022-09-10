"""CLI operations for taxonomy (Finnish: taksonomia) guided by conventions of a folder tree.."""
import argparse
import pathlib
import sys
from typing import List, Union

import taksonomia.taksonomia as api
from taksonomia import APP_ALIAS, APP_NAME


def parse_request(argv: List[str]) -> argparse.Namespace:
    """DRY."""
    parser = argparse.ArgumentParser(prog=APP_ALIAS, description=APP_NAME)
    parser.add_argument(
        '--tree-root',
        '-t',
        dest='tree_root',
        default='',
        help='tree root',
        required=False,
    )
    parser.add_argument('tree_root_pos', nargs='?', default='')
    parser.add_argument(
        '--out-path',
        '-o',
        dest='out_path',
        default=sys.stdout,
        help=('output file path for taxonomy (default: STDOUT)'),
    )
    options = parser.parse_args(argv)

    if not options.tree_root:
        if options.tree_root_pos:
            options.tree_root = options.tree_root_pos
        else:
            options.tree_root = str(pathlib.Path.cwd())

    tree_root = pathlib.Path(options.tree_root)
    if tree_root.exists():
        if tree_root.is_dir():
            return options
        print(f'ERROR: requested tree root at ({tree_root}) is not a folder', file=sys.stderr)
        parser.print_usage()
        sys.exit(1)

    print(f'ERROR: requested tree root at ({tree_root}) does not exist', file=sys.stderr)
    parser.print_usage()
    sys.exit(1)


def main(argv: Union[List[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    options = parse_request(argv)
    return api.main(options)
