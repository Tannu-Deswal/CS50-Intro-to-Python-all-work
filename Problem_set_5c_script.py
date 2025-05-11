#Re-requesting a Vanity Plate
import pytest
from Problem_set_5c import is_valid
def test_is_valid():
    assert is_valid('HELLO') == True
    assert is_valid('hie1') == True