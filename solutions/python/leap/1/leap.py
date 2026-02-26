def leap_year(year):
    leap_year = False
    if year % 4 != 0:
        leap_year = leap_year
    elif year % 100 == 0 and year % 400 != 0:
        leap_year = leap_year
    else:
        leap_year = True
    return leap_year
