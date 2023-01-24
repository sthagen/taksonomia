"""Taxonomy (Finnish: taksonomia) of a folder tree, guided by conventions."""
import datetime as dti
import logging
import os
import pathlib
from typing import List, no_type_check

# [[[fill git_describe()]]]
__version__ = '2023.1.10+parent.b82f6474'
# [[[end]]] (checksum: 6aefb8cc3095b51049d40c605d6a8819)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)

APP_ALIAS = 'taksonomia'
APP_ENV = 'TAKSONOMIA'
APP_NAME = 'Taxonomy (Finnish: taksonomia) of a folder tree, guided by conventions.'
APP_VERSION = __version__
COMMA = ','
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
DEFAULT_CONFIG_NAME = '.taksonomia.json'
DEFAULT_LF_ONLY = 'YES'
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
KNOWN_FORMATS = ('json', 'xml', 'yaml')
KNOWN_KEY_FUNCTIONS = ('elf', 'md5')
QUIET = False
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
TS_FORMAT = '%Y-%m-%d %H:%M:%S.%f +00:00'
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))
VERSION_INFO = __version_info__

log = logging.getLogger()  # Module level logger is sufficient
LOG_FOLDER = pathlib.Path('logs')
LOG_FILE = f'{APP_ALIAS}.log'
LOG_PATH = pathlib.Path(LOG_FOLDER, LOG_FILE) if LOG_FOLDER.is_dir() else pathlib.Path(LOG_FILE)
LOG_LEVEL = logging.INFO

TS_FORMAT_LOG = '%Y-%m-%dT%H:%M:%S'
TS_FORMAT_PAYLOADS = '%Y-%m-%d %H:%M:%S.%f UTC'

__all__: List[str] = [
    'APP_ALIAS',
    'APP_ENV',
    'APP_NAME',
    'APP_VERSION',
    'ENCODING',
    'TS_FORMAT_PAYLOADS',
    'VERSION_INFO',
    'log',
]


def parse_csl(csl: str) -> List[str]:
    """DRY."""
    return [fmt.strip().lower() for fmt in csl.split(COMMA) if fmt.strip()]


@no_type_check
def formatTime_RFC3339(self, record, datefmt=None):
    """HACK A DID ACK we could inject .astimezone() to localize ..."""
    return dti.datetime.fromtimestamp(record.created, dti.timezone.utc).isoformat()


@no_type_check
def init_logger(name=None, level=None):
    """Initialize module level logger"""
    global log  # pylint: disable=global-statement

    log_format = {
        'format': '%(asctime)s %(levelname)s [%(name)s]: %(message)s',
        'datefmt': TS_FORMAT_LOG,
        # 'filename': LOG_PATH,
        'level': LOG_LEVEL if level is None else level,
    }
    logging.Formatter.formatTime = formatTime_RFC3339
    logging.basicConfig(**log_format)
    log = logging.getLogger(APP_ENV if name is None else name)
    log.propagate = True


init_logger(name=APP_ENV, level=logging.DEBUG if DEBUG else None)
