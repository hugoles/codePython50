import numb3rs

def test_numb3rs():
    assert numb3rs.validate('192.168.1.1') == True
    assert numb3rs.validate('10.0.0.255') == True
    assert numb3rs.validate('256.168.1.1') == False
    assert numb3rs.validate('192.168.1.256') == False
    assert numb3rs.validate('192.168.1') == False
    assert numb3rs.validate('192.168.1.1.1') == False
    assert numb3rs.validate('192.168.1.') == False

