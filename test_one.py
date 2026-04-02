def test_one_file_exists():
    with open('one.txt', 'r') as f:
        content = f.read()
    assert content == 'This is a new one.txt file.'
