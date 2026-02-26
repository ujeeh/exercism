def leap_year(year):
    leap_year_state = False
    if year % 4 != 0:
        leap_year_state = False
    elif year % 100 == 0 and year % 400 != 0:
        leap_year_state = False
    else:
        leap_year_state = True
    return leap_year_state
