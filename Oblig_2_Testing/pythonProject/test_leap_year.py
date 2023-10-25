import pytest
from leap_year import is_leap_year

# Test year divisible by 4 but not by 100
def test_year_divisible_by_4_not_100():
    assert is_leap_year(2004) == True

# Test year not divisible by 4
def test_year_not_divisible_by_4():
    assert is_leap_year(2003) == False

# Test year divisible by 100 but not by 400
def test_year_divisible_by_100_not_400():
    assert is_leap_year(1900) == False

# Test year divisible by 400
def test_year_divisible_by_400():
    assert is_leap_year(2000) == True
