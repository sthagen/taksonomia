"""Taxonomy (Finnish: taksonomia) guided by conventions of a folder tree."""
import os
from typing import List

APP_NAME = 'Taxonomy (Finnish: taksonomia) guided by conventions of a folder tree.'
APP_ALIAS = 'taksonomia'
APP_ENV = 'TAKSONOMIA'
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))
QUIET = False
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
DEFAULT_CONFIG_NAME = '.taksonomia.json'
DEFAULT_LF_ONLY = 'YES'

# [[[fill git_describe()]]]
__version__ = '2022.9.10+parent.f142b795'
# [[[end]]] (checksum: 73350df0f894090b087006722919489b)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
__all__: List[str] = []
