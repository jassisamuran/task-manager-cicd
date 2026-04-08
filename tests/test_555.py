def test_file_exists():
    import os
    assert os.path.exists('555.txt')


def test_file_content():
    with open('555.txt', 'r') as f:
        content = f.read()
    assert content == ''  # Assuming the file is empty
