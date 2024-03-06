import fuel
import pytest

def test_fuel():
    with pytest.raises(ValueError):
        fuel.convert("6/3")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("0/0")
    with pytest.raises(ValueError):
        fuel.convert("12/4")
    assert fuel.convert("1/5") == 20


    assert fuel.gauge(99) == 'F'
    assert fuel.gauge(1) == 'E'
    assert fuel.gauge(50) == '50%'
    assert fuel.gauge(30) == '30%'
    assert fuel.gauge(25) == '25%'
