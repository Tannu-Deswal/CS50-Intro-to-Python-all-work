#Regualar, um, Expressions
import pytest
from Problem_set_7d import count
def test_count():
    assert count('um, yummy, um hie') == 2
    assert count('um UM Um') == 3
    assert count('this is me') == 0
    assert count('umumum um') == 1