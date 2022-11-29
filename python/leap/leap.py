def leap_year(year):

    status = 'none'

    if year % 4 == 0:
        status = 'one'
    if year % 4 == 0 and year % 100 == 0:
        status = 'two'
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        status = 'three'

    if status == 'one' or status == 'three':
        return True
    else:
        return False




    
        