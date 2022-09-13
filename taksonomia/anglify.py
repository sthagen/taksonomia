"""Transform taxonomy to XML."""
import collections.abc
import numbers
import xml.etree.ElementTree as ET  # nosec B405
from random import randint
from typing import no_type_check
from xml.dom.minidom import parseString  # nosec B408

from taksonomia import ENCODING

UNIQUE_IDS = []  # type: ignore


@no_type_check
def make_id(element, start=100000, end=999999):
    """Returns a random integer"""
    return '%s_%s' % (element, randint(start, end))  # nosec B311


@no_type_check
def get_unique_id(element):
    """Returns a unique id for a given element"""
    this_id = make_id(element)
    dup = True
    while dup:
        if this_id not in UNIQUE_IDS:
            dup = False
            UNIQUE_IDS.append(this_id)
        else:
            this_id = make_id(element)
    return UNIQUE_IDS[-1]


@no_type_check
def get_xml_type(val):
    """Returns the data type for the xml type attribute"""
    if type(val).__name__ == 'str':
        return 'str'
    if type(val).__name__ == 'int':
        return 'int'
    if type(val).__name__ == 'float':
        return 'float'
    if type(val).__name__ == 'bool':
        return 'bool'
    if isinstance(val, numbers.Number):
        return 'number'
    if type(val).__name__ == 'NoneType':
        return 'null'
    if isinstance(val, dict):
        return 'dict'
    if isinstance(val, collections.abc.Iterable):
        return 'list'
    return type(val).__name__


@no_type_check
def escape_xml(s):
    if type(s) == str:
        s = str(s)
        s = s.replace('&', '&amp;')
        s = s.replace('"', '&quot;')
        s = s.replace("'", '&apos;')
        s = s.replace('<', '&lt;')
        s = s.replace('>', '&gt;')
    return s


@no_type_check
def make_attrstring(attr):
    """Returns an attribute string in the form key="val" """
    attrstring = ' '.join(['%s="%s"' % (k, v) for k, v in attr.items()])
    return '%s%s' % (' ' if attrstring != '' else '', attrstring)


@no_type_check
def key_is_valid_xml(key):
    """Checks that a key is a valid XML name"""
    test_xml = '<?xml version="1.0" encoding="UTF-8" ?><%s>foo</%s>' % (key, key)
    try:
        parseString(test_xml)  # nosec B318
        return True
    except Exception:  # minidom does not implement exceptions well
        return False


@no_type_check
def make_valid_xml_name(key, attr):
    """Tests an XML name and fixes it if invalid"""
    key = escape_xml(key)
    attr = escape_xml(attr)

    # pass through if key is already valid
    if key_is_valid_xml(key):
        return key, attr

    # prepend a lowercase n if the key is numeric
    if key.isdigit():
        return 'n%s' % (key), attr

    # replace spaces with underscores if that fixes the problem
    if key_is_valid_xml(key.replace(' ', '_')):
        return key.replace(' ', '_'), attr

    # key is still invalid - move it into a name attribute
    attr['name'] = key
    key = 'key'
    return key, attr


@no_type_check
def wrap_cdata(s):
    """Wraps a string into CDATA sections"""
    s = str(s).replace(']]>', ']]]]><![CDATA[>')
    return '<![CDATA[' + s + ']]>'


@no_type_check
def default_item_func(parent):
    return 'item'


@no_type_check
def convert(obj, ids, attr_type, item_func, cdata, parent='root'):
    """Routes the elements of an object to the right function to convert them
    based on their data type"""

    item_name = item_func(parent)

    if isinstance(obj, numbers.Number) or type(obj) == str:
        return convert_kv(item_name, obj, attr_type, cdata)

    if hasattr(obj, 'isoformat'):
        return convert_kv(item_name, obj.isoformat(), attr_type, cdata)

    if type(obj) == bool:
        return convert_bool(item_name, obj, attr_type, cdata)

    if obj is None:
        return convert_none(item_name, '', attr_type, cdata)

    if isinstance(obj, dict):
        return convert_dict(obj, ids, parent, attr_type, item_func, cdata)

    if isinstance(obj, collections.abc.Iterable):
        return convert_list(obj, ids, parent, attr_type, item_func, cdata)

    raise TypeError('Unsupported data type: %s (%s)' % (obj, type(obj).__name__))


@no_type_check
def convert_dict(obj, ids, parent, attr_type, item_func, cdata):
    """Converts a dict into an XML string."""
    lines = []
    for key, val in obj.items():
        attr = {} if not ids else {'id': '%s' % (get_unique_id(parent))}

        key, attr = make_valid_xml_name(key, attr)

        if isinstance(val, numbers.Number) or type(val) == str:
            lines.append(convert_kv(key, val, attr_type, attr, cdata))

        elif hasattr(val, 'isoformat'):  # datetime
            lines.append(convert_kv(key, val.isoformat(), attr_type, attr, cdata))

        elif type(val) == bool:
            lines.append(convert_bool(key, val, attr_type, attr, cdata))

        elif isinstance(val, dict):
            if attr_type:
                attr['type'] = get_xml_type(val)
            lines.append(
                '<%s%s>%s</%s>'
                % (key, make_attrstring(attr), convert_dict(val, ids, key, attr_type, item_func, cdata), key)
            )

        elif isinstance(val, collections.abc.Iterable):
            if attr_type:
                attr['type'] = get_xml_type(val)
            lines.append(
                '<%s%s>%s</%s>'
                % (key, make_attrstring(attr), convert_list(val, ids, key, attr_type, item_func, cdata), key)
            )

        elif val is None:
            lines.append(convert_none(key, val, attr_type, attr, cdata))

        else:
            raise TypeError('Unsupported data type: %s (%s)' % (val, type(val).__name__))

    return ''.join(lines)


@no_type_check
def convert_list(items, ids, parent, attr_type, item_func, cdata):
    """Converts a list into an XML string."""
    lines = []

    item_name = item_func(parent)

    if ids:
        this_id = get_unique_id(parent)

    for i, item in enumerate(items):
        attr = {} if not ids else {'id': '%s_%s' % (this_id, i + 1)}
        if isinstance(item, numbers.Number) or type(item) == str:
            lines.append(convert_kv(item_name, item, attr_type, attr, cdata))

        elif hasattr(item, 'isoformat'):  # datetime
            lines.append(convert_kv(item_name, item.isoformat(), attr_type, attr, cdata))

        elif type(item) == bool:
            lines.append(convert_bool(item_name, item, attr_type, attr, cdata))

        elif isinstance(item, dict):
            if not attr_type:
                lines.append(
                    '<%s>%s</%s>'
                    % (
                        item_name,
                        convert_dict(item, ids, parent, attr_type, item_func, cdata),
                        item_name,
                    )
                )
            else:
                lines.append(
                    '<%s type="dict">%s</%s>'
                    % (
                        item_name,
                        convert_dict(item, ids, parent, attr_type, item_func, cdata),
                        item_name,
                    )
                )

        elif isinstance(item, collections.abc.Iterable):
            if not attr_type:
                lines.append(
                    '<%s %s>%s</%s>'
                    % (
                        item_name,
                        make_attrstring(attr),
                        convert_list(item, ids, item_name, attr_type, item_func, cdata),
                        item_name,
                    )
                )
            else:
                lines.append(
                    '<%s type="list"%s>%s</%s>'
                    % (
                        item_name,
                        make_attrstring(attr),
                        convert_list(item, ids, item_name, attr_type, item_func, cdata),
                        item_name,
                    )
                )

        elif item is None:
            lines.append(convert_none(item_name, None, attr_type, attr, cdata))

        else:
            raise TypeError('Unsupported data type: %s (%s)' % (item, type(item).__name__))
    return ''.join(lines)


@no_type_check
def convert_kv(key, val, attr_type, attr={}, cdata=False):
    """Converts a number or string into an XML element"""
    key, attr = make_valid_xml_name(key, attr)

    if attr_type:
        attr['type'] = get_xml_type(val)
    attrstring = make_attrstring(attr)
    return '<%s%s>%s</%s>' % (key, attrstring, wrap_cdata(val) if cdata else escape_xml(val), key)


@no_type_check
def convert_bool(key, val, attr_type, attr={}, cdata=False):
    """Converts a boolean into an XML element"""
    key, attr = make_valid_xml_name(key, attr)

    if attr_type:
        attr['type'] = get_xml_type(val)
    attrstring = make_attrstring(attr)
    return '<%s%s>%s</%s>' % (key, attrstring, str(val).lower(), key)


@no_type_check
def convert_none(key, val, attr_type, attr={}, cdata=False):
    """Converts a null value into an XML element"""
    key, attr = make_valid_xml_name(key, attr)

    if attr_type:
        attr['type'] = get_xml_type(val)
    attrstring = make_attrstring(attr)
    return '<%s%s></%s>' % (key, attrstring, key)


@no_type_check
def as_xml(obj, ids=False, attr_type=False, item_func=default_item_func, cdata=False):
    """Converts taxonomy tree into annotated XML."""
    lines = ['<?xml version="1.0" encoding="utf-8" ?>'] + [convert(obj, ids, attr_type, item_func, cdata, parent='')]
    x = ''.join(lines).encode(ENCODING)
    element = ET.XML(x)
    ET.indent(element)
    return '<?xml version="1.0" encoding="utf-8" ?>\n' + ET.tostring(element, encoding='unicode') + '\n'
