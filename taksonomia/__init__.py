"""Taxonomy (Finnish: taksonomia) guided by conventions of a folder tree."""
import os
from typing import List

APP_ALIAS = 'taksonomia'
APP_ENV = 'TAKSONOMIA'
APP_NAME = 'Taxonomy (Finnish: taksonomia) guided by conventions of a folder tree.'
COMMA = ','
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
DEFAULT_CONFIG_NAME = '.taksonomia.json'
DEFAULT_LF_ONLY = 'YES'
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
KNOWN_FORMATS = ('json', 'yaml')
QUIET = False
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
TS_FORMAT = '%Y-%m-%d %H:%M:%S.%f +00:00'
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))

# [[[fill git_describe()]]]
__version__ = '2022.9.11+parent.af6df604'
# [[[end]]] (checksum: 9336d94d5ff3d191250df64292d4a210)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
__all__: List[str] = []
