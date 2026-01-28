from src.math_operation import sub, add
import pytest

def test_add():
    assert add(2,3) == 5
    assert add(4,3) == 7
    assert add(2,2) == 4
    assert add(2,0) == 2


def test_sub():
    assert add(2,3) == -1
    assert add(4,3) == 1
    assert add(2,2) == 0
    assert add(2,0) == 2