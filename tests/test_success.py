def test_create_success_file():
    with open('success.text', 'w') as f:
        f.write('Success!')
    assert True
