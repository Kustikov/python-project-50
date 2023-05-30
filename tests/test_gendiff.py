from gendiff import generate_diff, get_dict


path1 = 'tests/fixtures/first_file.json'
path2 = 'tests/fixtures/second_file.json'
path3 = 'tests/fixtures/first_file.yaml'
path4 = 'tests/fixtures/second_file.yaml'
path5 = 'tests/fixtures/nested_1.json'
path6 = 'tests/fixtures/nested_2.json'

def test_get_dict_first():
    dict_json = get_dict(path1)
    dict_yaml = get_dict(path3)
    assert type(dict_json) == dict
    assert type(dict_yaml) == dict
    assert dict_json == {'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22', 'timeout': 50}
    assert dict_yaml == {'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22', 'timeout': 50}

def test_get_dict_second():
    dict_2 = get_dict(path2)
    assert type(dict_2) == dict
    assert dict_2 == {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
  }
def test_generate_diff_json():
    dict_1 = get_dict(path1)
    dict_2 = get_dict(path2)
    diff = generate_diff(dict_1, dict_2)
    assert type(diff) == dict
    assert diff == {'follow': {'type': 'deleted', 'value': False}, 'host': {'type': 'unchanged', 'value': 'hexlet.io'}, 'proxy': {'type': 'deleted', 'value': '123.234.53.22'}, 'timeout': {'type': 'changed', 'old_value': 50, 'new_value': 20}, 'verbose': {'type': 'added', 'value': True}}


def test_generate_diff_yaml():
    dict_1 = get_dict(path3)
    dict_2 = get_dict(path4)
    diff = generate_diff(dict_1, dict_2)
    assert type(diff) == dict
    assert diff == {'follow': {'type': 'deleted', 'value': False}, 'host': {'type': 'unchanged', 'value': 'hexlet.io'}, 'proxy': {'type': 'deleted', 'value': '123.234.53.22'}, 'timeout': {'type': 'changed', 'old_value': 50, 'new_value': 20}, 'verbose': {'type': 'added', 'value': True}}


def test_generate_diff_nested():
    dict_1 = get_dict(path5)
    dict_2 = get_dict(path6)
    diff = generate_diff(dict_1, dict_2)
    assert type(diff) == dict



    