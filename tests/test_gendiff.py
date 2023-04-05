from gendiff import generate_diff


path1 = './gendiff/json_files/first_file.json'
path2 =  './gendiff/json_files/first_file.json'


def test_diff():
    diff = generate_diff(path1, path2)
    print(diff)
    assert type(diff) == str
