#Back to the Bank
from Problem_set_5b import value
def test_value():
    assert value('Hello, there') == '$0'
    assert value('Hie there') == '$20'
    assert value('no hies') == '$100'