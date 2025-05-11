#Seasons of Love
#Valid just for today(04-05-2025)
from datetime import date
import pytest
from Problem_set_8a import convert, parse_date
def test_convert():
    assert convert(date(1999, 1, 1)) == 'Thirteen million, eight hundred fifty-two thousand, eight hundred minutes'
    
def test_parse_date_valid():
    assert parse_date("1999-01-01") == date(1999, 1, 1)

def test_parse_date_invalid_format():
    with pytest.raises(ValueError):
        parse_date("January 1, 1999")

def test_parse_date_future():
    with pytest.raises(ValueError):
        parse_date("3000-01-01")
    