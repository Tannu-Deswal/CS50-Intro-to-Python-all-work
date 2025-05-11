#Testing my twttr
import pytest
from Problem_set_5a import shorten
def test_shorten():
    assert shorten('Hello.') == 'Hll.'