import os
import pytest


def test_add_file():
    # Check if the file 9.txt exists
    assert os.path.isfile('9.txt')

    # Check if the file is not empty
    assert os.path.getsize('9.txt') > 0
