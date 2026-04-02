def test_file_exists():
    import os
    assert os.path.exists('900.txt')


def test_file_content():
    with open('900.txt', 'r') as f:
        content = f.read()
    assert content == ''  # Assuming the file is empty
