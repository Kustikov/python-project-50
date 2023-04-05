from gendiff import generate_diff

path1 = './gendiff/json_files/first_file.json'
path2 = './gendiff/json_files/second_file.json'


def test_diff():
    diff = generate_diff(path1, path2)
    assert type(diff) == str
    assert diff == '{\n + follow: False\n   host: hexlet.io\n + proxy: 123.234.53.22\n + timeout: 50\n - timeout: 20\n - verbose: True\n}'
    
    