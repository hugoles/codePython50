import seasons
import pytest

def test():
    assert seasons.seasons('2002-10-01') == 'Eleven million, two hundred eight thousand, nine hundred sixty minutes'
    assert seasons.seasons('2022-01-23') == 'One million, fifty-one thousand, two hundred minutes'
    with pytest.raises(SystemExit):
        seasons.seasons('2001--19')
