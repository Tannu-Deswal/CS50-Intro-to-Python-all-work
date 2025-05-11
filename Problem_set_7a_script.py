#NUMB3RS
import pytest
from Problem_set_7a import validate
def test_validate():
    assert validate('255.255.255.255') == True
    assert validate('0.1.56.219') == True