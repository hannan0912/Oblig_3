def is_leap_year(year: int) -> bool:
    """Check if a year is a leap year based on Gregorian calendar rules."""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
