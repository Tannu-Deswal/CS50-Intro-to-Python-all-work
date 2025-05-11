#Working 9 to 5
import pytest
from Problem_set_7c import convert
def test_convert():
    assert convert('9 am to 5 pm') == '09:00 to 17:00'
    assert convert('10 am to 8:30 pm') == '10:00 to 20:30'