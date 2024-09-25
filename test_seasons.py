from seasons import BornDate
from datetime import date
import pytest

def test_years():
    today = date.today()
    borndate = BornDate(today.year-2, today.month, today.day)
    assert borndate.season_time() in ('One million, fifty-one thousand, two hundred minutes',
                                    'One million, fifty-two thousand, six hundred forty minutes')
    
    borndate = BornDate(today.year-1, today.month, today.day)
    assert borndate.season_time() in ('Five hundred twenty-five thousand, six hundred minutes',
                                    'Five hundred twenty-seven thousand forty minutes')

def test_wrong_valur():
    year, month, day = [1990,13,1]
    with pytest.raises(ValueError):
        BornDate(year, month, day)
    
    year, month, day = [1990,12,32]
    with pytest.raises(ValueError):
        BornDate(year, month, day)
    
    year, month, day = [1990,2,30]
    with pytest.raises(ValueError):
        BornDate(year, month, day)