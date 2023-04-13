from gendiff import generate_diff


path1 = 'tests/fixtures/first_file.json'
path2 = 'tests/fixtures/second_file.json'
path3 = 'tests/fixtures/first_file.yaml'
path4 = 'tests/fixtures/second_file.yaml'



def test_diff():
    diff = generate_diff(path1, path2)
    assert type(diff) == list
    assert len(path1) > 0
    assert len(path2) > 0
    assert path1[-4:] == 'json'
    assert path2[-4:] == 'json'
    assert diff == [{'name': 'follow', 'value': False, 'type': 'deleted'}, {'name': 'host', 'value': 'hexlet.io', 'type': 'unchanged'}, {'name': 'proxy', 'value': '123.234.53.22', 'type': 'deleted'}, {'name': 'timeout', 'value1': 50, 'value2': 20, 'type': 'changed'}, {'name': 'verbose', 'value': True, 'type': 'added'}]


def test_diff():
    diff = generate_diff(path3, path4)
    assert type(diff) == list
    assert len(path1) > 0
    assert len(path2) > 0
    assert path1[-4:] == 'json'
    assert path2[-4:] == 'json'
    assert diff == [{'name': 'follow', 'value': False, 'type': 'deleted'}, {'name': 'host', 'value': 'hexlet.io', 'type': 'unchanged'}, {'name': 'proxy', 'value': '123.234.53.22', 'type': 'deleted'}, {'name': 'timeout', 'value1': 50, 'value2': 20, 'type': 'changed'}, {'name': 'verbose', 'value': True, 'type': 'added'}]






    