#Cookie Jar
import pytest
from Problem_set_8b import Jar


def test_init():
    jar = Jar(11)
    assert jar._capacity == 11


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar._size == 3
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(1)
    assert jar._size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)