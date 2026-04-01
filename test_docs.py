def test_docs_content():
    with open('docs.txt', 'r') as file:
        content = file.read().strip()
    assert content == 'my name is ai agent'