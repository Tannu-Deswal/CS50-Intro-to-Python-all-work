# Refueling
import pytest
from Problem_set_5d import convert, gauge

def test_convert():
    assert convert('1/4') == 0.25
    assert convert('3/4') == 0.75
    assert convert('1/2') == 0.5

def test_gauge():
    assert gauge(0.25) == '25%'
    assert gauge(0.01) == 'E'
    assert gauge(0.99) == 'F'

def test_convert_error():
    with pytest.raises(ValueError):
        convert('cat')  # wrong format
    with pytest.raises(ValueError):
        convert('2/1')  # x > y
    with pytest.raises(ValueError):
        convert('1/0')  # division by zero