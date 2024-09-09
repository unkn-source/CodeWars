def year_days(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days = 366
    else:
        days = 365
    return f"{year} has {days} days"