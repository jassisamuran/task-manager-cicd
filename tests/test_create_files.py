def test_create_files():
    with open('1.txt', 'w') as f:
        f.write('This is 1.txt')
    with open('2.txt', 'w') as f:
        f.write('This is 2.txt')
