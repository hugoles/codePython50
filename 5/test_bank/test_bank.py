import bank

def test_bank():
    assert bank.value("Hello") == 0
    assert bank.value("hugo") == 20
    assert bank.value("Abracadabra sim salabim") == 100
