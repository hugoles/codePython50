from twttr import shorten

def test_twttr():
    assert shorten("aeiou") == ''
    assert shorten("Dr. Ines de Castro Dutra") == 'Dr. ns d Cstr Dtr'
    assert shorten("1234567890") == "1234567890"
