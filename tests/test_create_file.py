def test_create_file():
    with open('2.txt', 'w') as f:
        f.write('This is a test file.')
    assert True  # Test passes if no exception occurs
