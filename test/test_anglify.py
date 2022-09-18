import taksonomia.anglify as api


def test_get_xml_type():
    pairs = (
        ('a', 'str'),
        (42, 'int'),
        (3.14156, 'float'),
        (True, 'bool'),
        (complex(0, 1), 'number'),
        (None, 'null'),
        ({}, 'dict'),
        ([], 'list'),
        (object(), 'object'),
    )
    for value, expected in pairs:
        assert api.get_xml_type(value) == expected


def test_get_unique_id():
    some_thing = api.get_unique_id('42')
    assert some_thing.startswith('42_')
    assert int(some_thing.split('_', 1)[1])


def test_make_valid_xml_name():
    key, attr = api.make_valid_xml_name('1234cafe', {})
    assert key == 'key'
    assert attr == {'id': '1234cafe'}

    key, attr = api.make_valid_xml_name('sha256', {})
    assert key == 'sha256'
    assert attr == {}

    key, attr = api.make_valid_xml_name('sha512', {})
    assert key == 'sha512'
    assert attr == {}

    key, attr = api.make_valid_xml_name('a256cafe', {})
    assert key == 'key'
    assert attr == {'id': 'a256cafe'}

    key, attr = api.make_valid_xml_name('-ohno', {})
    assert key == 'key'
    assert attr == {'name': '-ohno'}

    key, attr = api.make_valid_xml_name(' ohno', {})
    assert key == '_ohno'
    assert attr == {}
