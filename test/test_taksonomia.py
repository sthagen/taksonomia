import pathlib
import re
import sys

import pytest

from taksonomia.taksonomia import Taxonomy, parse


def test_taxonomy_hash_file_bad_algo():
    folder = pathlib.Path('test', 'fixtures', 'corner')
    taxonomy = Taxonomy(folder, 'me,too')
    message = '"Unsupported hash algorithm requested - foo is not in (\'sha512\', \'sha256\')"'
    with pytest.raises(KeyError, match=re.escape(message)):
        taxonomy.hash_file(folder / 'empty.txt', 'foo')


def test_taxonomy_repr():
    folder = pathlib.Path('test', 'fixtures', 'corner')
    taxonomy = Taxonomy(folder, 'me,too')
    assert str(taxonomy)


def test_taxonomy_close():
    folder = pathlib.Path('test', 'fixtures', 'corner')
    taxonomy = Taxonomy(folder, 'me,too')
    assert not taxonomy.closed
    taxonomy.close()
    end_ts = taxonomy.tree['taxonomy']['context']['end_ts']
    duration_usecs = taxonomy.tree['taxonomy']['context']['duration_usecs']
    assert taxonomy.closed
    taxonomy.close()
    assert taxonomy.tree['taxonomy']['context']['end_ts'] == end_ts
    assert taxonomy.tree['taxonomy']['context']['duration_usecs'] == duration_usecs


def test_taxonomy_report_screen_only():
    folder = pathlib.Path('test', 'fixtures', 'corner')
    taxonomy = Taxonomy(folder, 'me,too')
    assert not taxonomy.closed
    assert taxonomy.tree['taxonomy']['context']['end_ts'] is None
    assert taxonomy.tree['taxonomy']['context']['duration_usecs'] == 0
    tree = taxonomy.report()
    assert taxonomy.tree['taxonomy']['context']['end_ts'] is not None
    assert taxonomy.tree['taxonomy']['context']['duration_usecs'] > 0
    assert tree['taxonomy']['context']['duration_usecs'] == taxonomy.tree['taxonomy']['context']['duration_usecs']


def test_taxonomy_yaml_to_stdout_screen_only():
    folder = pathlib.Path('test', 'fixtures', 'corner')
    taxonomy = Taxonomy(folder, 'me,too')
    taxonomy.dump(sink=sys.stdout, format_type='yaml')


def test_taxonomy_yaml_to_stdout_screen_only_base64():
    folder = pathlib.Path('test', 'fixtures', 'corner')
    taxonomy = Taxonomy(folder, 'me,too')
    taxonomy.dump(sink=sys.stdout, format_type='yaml', base64_encode=True)


def test_taxonomy_json_to_stdout_screen_only_base64():
    folder = pathlib.Path('test', 'fixtures', 'corner')
    taxonomy = Taxonomy(folder, 'me,too')
    taxonomy.dump(sink=sys.stdout, format_type='json', base64_encode=True)


def test_taxonomy_dump_bad_format():
    folder = pathlib.Path('test', 'fixtures', 'corner')
    taxonomy = Taxonomy(folder, 'me,too')
    message = r"requested format unknown for taxonomy dump not in ('json', 'yaml')"
    with pytest.raises(ValueError, match=re.escape(message)):
        taxonomy.dump(sink=sys.stdout, format_type='unknown')


def test_parse():
    assert parse() is NotImplemented
