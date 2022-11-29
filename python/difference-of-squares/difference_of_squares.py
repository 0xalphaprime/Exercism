def square_of_sum(number):
    number = number
    total_sum = 0
    while number > 0:
        total_sum += number
        number -= 1

    return total_sum**2


print(square_of_sum(3))


def sum_of_squares(number):
    number = number
    total_squared = 0
    while number > 0:
        total_squared += number**2
        number -= 1

    return total_squared


def difference_of_squares(number):
    difference = square_of_sum(number) - sum_of_squares(number)
    return difference
