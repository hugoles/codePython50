import plates

def test_plates():
    assert plates.is_valid('123456') == False
    assert plates.is_valid('a') == False
    assert plates.is_valid('ab13a5') == False
    assert plates.is_valid('0xp222') == False
    assert plates.is_valid('v02796') == False
    assert plates.is_valid('rb2395') == True
    assert plates.is_valid('asd2356') ==False
    assert plates.is_valid('asd032') == False
    assert plates.is_valid('ab@%#') == False
