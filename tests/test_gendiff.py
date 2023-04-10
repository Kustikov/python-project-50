from gendiff import generate_diff


path1 = 'tests/fixtures/first_file.json'
path2 = 'tests/fixtures/second_file.json'
path3 = 'tests/fixtures/first_file.yaml'
path4 = 'tests/fixtures/second_file.yaml'



def test_diff():
    diff = generate_diff(path1, path2)
    assert type(diff) == str
    assert len(path1) > 0
    assert len(path2) > 0
    assert path1[-4:] == 'json'
    assert path2[-4:] == 'json'
    assert diff == '{\n - follow: False\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: True\n}'


def test_diff():
    diff = generate_diff(path3, path4)
    assert type(diff) == str
    assert len(path1) > 0
    assert len(path2) > 0
    assert path1[-4:] == 'json'
    assert path2[-4:] == 'json'
    assert diff == '{\n - follow: False\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: True\n}'






    