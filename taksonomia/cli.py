"""CLI operations for taxonomy (Finnish: taksonomia) of a folder tree, guided by conventions."""
import argparse
import pathlib
import sys
from typing import List, Union

import taksonomia.taksonomia as api
from taksonomia import APP_ALIAS, APP_NAME, KNOWN_FORMATS, KNOWN_KEY_FUNCTIONS, parse_csl


def parse_request(argv: List[str]) -> Union[int, argparse.Namespace]:
    """DRY."""
    parser = argparse.ArgumentParser(
        prog=APP_ALIAS, description=APP_NAME, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--tree-root',
        '-t',
        dest='tree_root',
        default='',
        help='Root of the tree to visit. Optional\n(default: positional tree root value)',
        required=False,
    )
    parser.add_argument(
        'tree_root_pos', nargs='?', default='', help='Root of the tree to visit. Optional (default: PWD)'
    )
    parser.add_argument(
        '--excludes',
        '-x',
        dest='excludes',
        default='',
        help='comma separated list of values to exclude paths\ncontaining the substring (default: empty string)',
    )
    parser.add_argument(
        '--key-function',
        '-k',
        dest='key_function',
        default='elf',
        help='key function (elf, md5) for branches and leaves\n(default: elf) use md5 for larger taxonomies',
    )
    parser.add_argument(
        '--out-path',
        '-o',
        dest='out_path',
        default=sys.stdout,
        help='output file path (stem) for taxonomy (default: STDOUT)',
    )
    parser.add_argument(
        '--formats',
        '-f',
        dest='format_type_csl',
        default='json',
        help='formats (json, xml, yaml) as comma separated list for taxonomy (default: json)',
    )
    parser.add_argument(
        '--base64-encode',
        '-e',
        dest='base64_encode',
        default=False,
        action='store_true',
        help='encode taxonomy in base64 (default: False)\nincompatible with option --xz-compress',
    )
    parser.add_argument(
        '--xz-compress',
        '-c',
        dest='xz_compress',
        default=False,
        action='store_true',
        help='compress taxonomy per LZMA(xz) (default: False)\nincompatible with option --base64-encode',
    )
    if not argv:
        parser.print_help()
        return 0

    options = parser.parse_args(argv)

    if not options.tree_root:
        if options.tree_root_pos:
            options.tree_root = options.tree_root_pos
        else:
            options.tree_root = str(pathlib.Path.cwd())

    if options.key_function.lower() not in KNOWN_KEY_FUNCTIONS:
        parser.error(
            f'requested key function {options.key_function} for branches and leaves not in {KNOWN_KEY_FUNCTIONS}'
        )

    format_types = parse_csl(options.format_type_csl)
    channel_count = len(format_types)
    for fmt in format_types:
        if fmt not in KNOWN_FORMATS:
            parser.error(f'requested format {fmt} for taxonomy dump not in {KNOWN_FORMATS}')

    if options.out_path is sys.stdout and channel_count > 1:
        parser.error('writing multiple formats to STDOUT is not supported.')

    if options.base64_encode and options.xz_compress:
        parser.error('the options --base64-encode and --xz-compress are mutually exclusive.')

    if options.xz_compress and options.out_path is sys.stdout:
        parser.error('compression for now not supported for standard output (only for files)')

    tree_root = pathlib.Path(options.tree_root)
    if tree_root.exists():
        if tree_root.is_dir():
            return options
        parser.error(f'requested tree root at ({tree_root}) is not a folder')

    parser.error(f'requested tree root at ({tree_root}) does not exist')


def main(argv: Union[List[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    options = parse_request(argv)
    if isinstance(options, int):
        return 0
    return api.main(options)
