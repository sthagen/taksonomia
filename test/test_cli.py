import pytest

import taksonomia.cli as cli


def test_parse_request(capsys):
    with pytest.raises(SystemExit) as err:
        cli.parse_request([])
    assert err.value.code == 2
    out, err = capsys.readouterr()
    assert 'the following arguments are required: --tree-root/-t' in out
    assert not err


def test_parse_request(capsys):
    for option in ('-h', '--help'):
        with pytest.raises(SystemExit) as err:
            cli.parse_request([option])
        assert not err.value.code
        out, err = capsys.readouterr()
        assert 'output file path for taxonomy' in out
        assert not err
