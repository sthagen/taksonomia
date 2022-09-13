import pathlib
import sys

import pytest

import taksonomia.cli as cli
import taksonomia.taksonomia as api
from taksonomia.taksonomia import EMPTY_SHA512, XZ_EXT


def test_parse_request_empty(capsys):
    options = cli.parse_request([])
    assert options.out_path is sys.stdout
    assert options.tree_root == str(pathlib.Path.cwd())
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_parse_request_help(capsys):
    for option in ('-h', '--help'):
        with pytest.raises(SystemExit) as err:
            cli.parse_request([option])
        assert not err.value.code
        out, err = capsys.readouterr()
        assert 'output file path for taxonomy' in out
        assert not err


def test_parse_request_non_existing_tree_root(capsys):
    with pytest.raises(SystemExit) as err:
        cli.parse_request(['--tree-root', 'this-tree-root-is-missing'])
    assert err.value.code == 2
    out, err = capsys.readouterr()
    assert 'usage: taksonomia [-h] [--tree-root TREE_ROOT] [--excludes EXCLUDES]' in err
    assert 'taksonomia: error: requested tree root at (this-tree-root-is-missing) does not exist' in err
    assert not out


def test_parse_request_non_existing_format(capsys):
    with pytest.raises(SystemExit) as err:
        cli.parse_request(['--tree-root', 'this-tree-root-is-missing', '--format', 'unknown'])
    assert err.value.code == 2
    out, err = capsys.readouterr()
    assert 'usage: taksonomia [-h] [--tree-root TREE_ROOT] [--excludes EXCLUDES]' in err
    assert "taksonomia: error: requested format unknown for taxonomy dump not in ('json', 'xml', 'yaml')" in err
    assert not out


def test_parse_request_file_as_tree_root(capsys):
    with pytest.raises(SystemExit) as err:
        cli.parse_request(['--tree-root', 'requirements.txt'])
    assert err.value.code == 2
    out, err = capsys.readouterr()
    assert 'usage: taksonomia [-h] [--tree-root TREE_ROOT] [--excludes EXCLUDES]' in err
    assert 'taksonomia: error: requested tree root at (requirements.txt) is not a folder' in err
    assert not out


def test_parse_request_tree_root_test_fixtures_corner(capsys):
    options = cli.parse_request(['--tree-root', 'test/fixtures/corner/', '-o', '/dev/null'])
    assert options.tree_root == 'test/fixtures/corner/'
    assert options.out_path == '/dev/null'
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_tree_root_test_fixtures_corner_nirvana(capsys):
    code = cli.main(['--tree-root', 'test/fixtures/corner/', '-o', '/dev/null'])
    assert code == 0
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_tree_root_pos_test_fixtures_corner_nirvana(capsys):
    code = cli.main(['test/fixtures/corner/', '-o', '/dev/null'])
    assert code == 0
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_tree_root_pos_test_fixtures_corner_nirvana_excludes(capsys):
    code = cli.main(['test/fixtures/corner/', '-o', '/dev/null', '-x', 'corner'])
    assert code == 0
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_tree_root_test_fixtures_corner_result(capsys):
    code = cli.main(['--tree-root', 'test/fixtures/corner/'])
    assert code == 0
    out, err = capsys.readouterr()
    assert f'"sha512": "{EMPTY_SHA512}",' in out
    assert '"count_branches": 0,' in out
    assert '"count_leaves": 1,' in out
    assert '"size_bytes": 0,' in out
    assert not err


def test_main_tree_root_test_fixtures_corner_result_excludes(capsys):
    code = cli.main(['--tree-root', 'test/fixtures/corner/', '--excludes', 'empty'])
    assert code == 0
    out, err = capsys.readouterr()
    assert f'"sha512": "{EMPTY_SHA512}",' in out
    assert '"count_branches": 0,' in out
    assert '"count_leaves": 0,' in out
    assert '"size_bytes": 0' in out
    assert not err


def test_main_tree_root_test_fixtures_basic_result(capsys):
    code = cli.main(['--tree-root', 'test/fixtures/basic/'])
    assert code == 0
    out, err = capsys.readouterr()
    assert '"sha512": "e7fa8661' in out
    assert '"count_branches": 4,' in out
    assert '"count_leaves": 8,' in out
    assert '"size_bytes": 15' in out
    assert not err


def test_main_tree_root_pos_test_fixtures_basic_nirvana_excludes(capsys):
    code = cli.main(['test/fixtures/basic/', '-o', '/dev/null', '-x', 'empty'])
    assert code == 0
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_tree_root_pos_test_fixtures_basic_nirvana_excludes_with_slash(capsys):
    code = cli.main(['test/fixtures/basic/', '-o', '/dev/null', '-x', 'empty,/'])
    assert code == 0
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_format_yaml_tree_root_pos_test_fixtures_basic_nirvana_excludes_with_slash(capsys):
    code = cli.main(['test/fixtures/basic/', '-o', '/dev/null', '-x', 'empty,/', '--format', 'yaml'])
    assert code == 0
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_format_yaml_tree_root_pos_test_fixtures_basic_nirvana_excludes_with_slash_base64(capsys):
    code = cli.main(['test/fixtures/basic/', '-o', '/dev/null', '-x', 'empty,/', '--format', 'yaml', '--base64-encode'])
    assert code == 0
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_compress_yaml(capsys):
    options = cli.parse_request(
        ['test/fixtures/basic/', '-c', '-o', '/tmp/delete-me.yml.xz', '-x', 'empty,/', '--format', 'yaml']
    )
    code = api.main(options)
    assert code == 0
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_compress_json(capsys):
    options = cli.parse_request(['test/fixtures/basic/', '-c', '-o', '/tmp/delete-me.json.xz', '-x', 'empty,/'])
    code = api.main(options)
    assert code == 0
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_compress_xml(capsys):
    options = cli.parse_request(
        ['test/fixtures/basic/', '-f', 'xml', '-c', '-o', '/tmp/delete-me.xml.xz', '-x', 'empty,/']
    )
    code = api.main(options)
    assert code == 0
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_xml(capsys):
    options = cli.parse_request(['test/fixtures/basic/', '-f', 'xml', '-o', '/tmp/delete-me.xml', '-x', 'empty,/'])
    code = api.main(options)
    assert code == 0
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_xml_stdout(capsys):
    options = cli.parse_request(['test/fixtures/basic/', '-f', 'xml', '-x', 'empty,/'])
    code = api.main(options)
    assert code == 0
    out, err = capsys.readouterr()
    assert '<?xml version="1.0" encoding="utf-8" ?>\n<taxonomy>' in out
    assert not err


def test_main_b64_encode_xml_stdout(capsys):
    options = cli.parse_request(['test/fixtures/basic/', '-e', '-f', 'xml', '-x', 'empty,/'])
    code = api.main(options)
    assert code == 0
    out, err = capsys.readouterr()
    assert out.startswith('PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiID8+')
    assert not err


def test_main_b64_encode_xml(capsys):
    options = cli.parse_request(
        ['test/fixtures/basic/', '-e', '-f', 'xml', '-o', '/tmp/delete-me.xml.base64', '-x', 'empty,/']
    )
    code = api.main(options)
    assert code == 0
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_encoding_and_compression_given(capsys):
    with pytest.raises(SystemExit) as err:
        cli.main(['test/fixtures/basic/', '-o', '/dev/null', '-e', '-c'])
    assert err.value.code == 2
    out, err = capsys.readouterr()
    assert 'usage: taksonomia [-h] [--tree-root TREE_ROOT] [--excludes EXCLUDES]' in err
    assert 'taksonomia: error: the options --base64-encode and --xz-compress are mutually exclusive' in err
    assert not out


def test_main_compression_and_stdout_given(capsys):
    with pytest.raises(SystemExit) as err:
        cli.main(['test/fixtures/basic/', '-c'])
    assert err.value.code == 2
    out, err = capsys.readouterr()
    assert 'usage: taksonomia [-h] [--tree-root TREE_ROOT] [--excludes EXCLUDES]' in err
    assert 'taksonomia: error: compression for now not supported for standard output (only for files)' in err
    assert not out


def test_main_compression_and_file_without_xz_suffix_given(capsys):
    with pytest.raises(SystemExit) as err:
        cli.main(['test/fixtures/basic/', '-o', '/tmp/some.json', '-c'])
    assert err.value.code == 2
    out, err = capsys.readouterr()
    assert 'usage: taksonomia [-h] [--tree-root TREE_ROOT] [--excludes EXCLUDES]' in err
    assert (
        f'taksonomia: error: compression for now only supported for output written to a file with {XZ_EXT} suffix'
        in err
    )
    assert not out


def test_main_unknown_key_function(capsys):
    with pytest.raises(SystemExit) as err:
        cli.main(['test/fixtures/basic/', '-k', 'unknown-key-function'])
    assert err.value.code == 2
    out, err = capsys.readouterr()
    assert 'usage: taksonomia [-h] [--tree-root TREE_ROOT] [--excludes EXCLUDES]' in err
    assert (
        "taksonomia: error: requested key function unknown-key-function for branches and leaves not in ('elf', 'md5')"
        in err
    )
    assert not out
