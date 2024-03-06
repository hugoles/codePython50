import working
import pytest

def test():
    assert working.convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert working.convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert working.convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'
    with pytest.raises(ValueError):
            working.convert('15:00 AM to 17:00 PM')
    with pytest.raises(ValueError):
            working.convert('15 to 17')
    with pytest.raises(ValueError):
            working.convert('15:00 AM to 17:80 PM')
    with pytest.raises(ValueError):
            working.convert('15:00 AM 17:80 PM')

