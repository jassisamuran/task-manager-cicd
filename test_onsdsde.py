def test_onsdsde_file_exists():
    import os
    assert os.path.exists('onsdsde.txt')


def test_onsdsde_file_non_empty():
    with open('onsdsde.txt', 'r') as f:
        content = f.read()
    assert len(content) > 0
