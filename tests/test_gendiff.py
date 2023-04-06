from gendiff import generate_diff


path1 = './tests/fixtures/first_file.json'
path2 = './tests/fixtures/second_file.json'
path3 = './tests/fixtures/third_file.json'
path4 = './tests/fixtures/fourth_file.json'


def test_diff():
    diff = generate_diff(path1, path2)
    assert type(diff) == str
    assert len(path1) > 0
    assert len(path2) > 0
    assert path1[-4:] == 'json'
    assert path2[-4:] == 'json'
    assert diff == '{\n + follow: False\n   host: hexlet.io\n + proxy: 123.234.53.22\n - timeout: 20\n + timeout: 50\n - verbose: True\n}'


def test_diff_2():
    diff = generate_diff(path3, path4)
    assert type(diff) == str
    assert len(path1) > 0
    assert len(path2) > 0
    assert path1[-4:] == 'json'
    assert path2[-4:] == 'json'
    assert diff == '{\n   common.device: {device, select, mobile {Mobile} desktop {Desktop} other {Other}}\n + common.formatted-date: {currDate, date, medium}\n   common.formatted-number: {num, number, ::compact-short}\n   common.items-counter: {count, plural, one {{count} item} other {{count} items}}\n   common.next: Next\n - common.ok: NO\n + common.ok: OK\n   common.previous: Previous\n + common.title-name: {gender, select, male {Mr. {name}} female {Ms. {name}} other {{name}}}\n + page.home.subtitle: Glad to see you {name}\n + page.home.title: Welcome\n - page.home.title: Welcome to site\n}'






    