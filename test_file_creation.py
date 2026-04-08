def test_file_creation():
    with open('one.txt', 'r') as f:
        content = f.read()
    assert content == 'one.txt'
