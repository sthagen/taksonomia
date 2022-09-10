"""Taxonomy (Finnish: taksonomia) guided by conventions of a folder tree."""
import os
from typing import List

APP_NAME = 'Taxonomy (Finnish: taksonomia) guided by conventions of a folder tree.'
APP_ALIAS = 'taksonomia'
APP_ENV = 'TAKSONOMIA'
COMMA = ','
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))
QUIET = False
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
DEFAULT_CONFIG_NAME = '.taksonomia.json'
DEFAULT_LF_ONLY = 'YES'
TS_FORMAT = '%Y-%m-%d %H:%M:%S.%f +00:00'

# [[[fill git_describe()]]]
__version__ = '2022.9.11+parent.af6df604'
# [[[end]]] (checksum: 9336d94d5ff3d191250df64292d4a210)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
__all__: List[str] = []
