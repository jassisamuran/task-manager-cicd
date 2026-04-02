def test_file_exists():
    with open('7889.text', 'r') as f:
        content = f.read()
    assert content is not None


def test_file_length():
    with open('7889.text', 'r') as f:
        content = f.read()
    assert len(content) > 0
