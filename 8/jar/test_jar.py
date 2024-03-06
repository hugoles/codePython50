from jar import Jar
import pytest

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():

    jar = Jar(5)
    assert jar.size == 0
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(2)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():

    jar = Jar(8)
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3
    jar.withdraw(3)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)
