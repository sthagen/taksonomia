import os
import pathlib

from taksonomia.machine import Machine


def test_machine():
    folder = pathlib.Path('test', 'fixtures', 'corner')
    pid = os.getpid()
    machine = Machine(str(folder), pid)
    assert str(machine)
    assert machine.context()
    assert machine.perf()
