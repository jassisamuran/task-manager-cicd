import pytest


def test_requirements_file():
    with open('requirements.txt', 'r') as f:
        content = f.read()
    assert '# Requirements for the project' in content
    assert '# List of dependencies' in content
    assert '# Example dependencies' in content
    assert 'requests==2.25.1' in content
    assert 'numpy==1.21.0' in content
