import pathlib
import re

import pytest

from taksonomia.taksonomia import Taxonomy, parse


def test_taxonomy_hash_file_bad_algo():
    folder = pathlib.Path('test', 'fixtures', 'corner')
    visit = Taxonomy(folder, 'me,too')
    message = '"Unsupported hash algorithm requested - foo is not in (\'sha512\', \'sha256\')"'
    with pytest.raises(KeyError, match=re.escape(message)):
        visit.hash_file(folder / 'empty.txt', 'foo')


def test_taxonomy_repr():
    folder = pathlib.Path('test', 'fixtures', 'corner')
    visit = Taxonomy(folder, 'me,too')
    assert str(visit)


def test_parse():
    assert parse() is NotImplemented
