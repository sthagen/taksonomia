import pytest

import taksonomia.cli as cli
from taksonomia.taksonomia import EMPTY_SHA512


def test_parse_request_empty(capsys):
    with pytest.raises(SystemExit) as err:
        cli.parse_request([])
    assert err.value.code == 2
    out, err = capsys.readouterr()
    assert not out
    assert 'the following arguments are required: --tree-root/-t' in err


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
    assert err.value.code == 1
    out, err = capsys.readouterr()
    assert '[-h] --tree-root TREE_ROOT [--out-path OUT_PATH]' in out
    assert 'ERROR: requested tree root at (this-tree-root-is-missing) does not exist' in err


def test_parse_request_file_as_tree_root(capsys):
    with pytest.raises(SystemExit) as err:
        cli.parse_request(['--tree-root', 'requirements.txt'])
    assert err.value.code == 1
    out, err = capsys.readouterr()
    assert '[-h] --tree-root TREE_ROOT [--out-path OUT_PATH]' in out
    assert 'ERROR: requested tree root at (requirements.txt) is not a folder' in err


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


def test_main_tree_root_test_fixtures_corner_result(capsys):
    code = cli.main(['--tree-root', 'test/fixtures/corner/'])
    assert code == 0
    out, err = capsys.readouterr()
    assert f'"sha512": "{EMPTY_SHA512}",' in out
    assert '"count_folders": 1,' in out
    assert '"count_files": 1,' in out
    assert '"size_bytes": 0,' in out
    assert not err
