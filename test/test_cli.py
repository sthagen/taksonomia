import pytest

import taksonomia.cli as cli


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


def test_parse_request_bad_tree_root(capsys):
    with pytest.raises(SystemExit) as err:
        cli.parse_request(['--tree-root', 'this-tree-root-is-missing'])
    assert err.value.code == 1
    out, err = capsys.readouterr()
    assert '[-h] --tree-root TREE_ROOT [--out-path OUT_PATH]' in out
    assert 'ERROR: requested tree root at (this-tree-root-is-missing) does not exist' in err
