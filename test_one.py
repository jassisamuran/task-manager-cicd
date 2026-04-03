def test_file_exists():
    import os
    assert os.path.isfile('one.text')


def test_file_content():
    with open('one.text', 'r') as f:
        content = f.read()
    assert content == ''  # Assuming the file is initially empty
