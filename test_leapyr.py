from leap_year import leapyear

def test_leapyr ():
    assert leapyear(2008) == "Leap year"

def test_leap_year ():
    assert leapyear(2025) == "Not a Leap year"