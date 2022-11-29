def is_armstrong_number(number):
    number_list = [int(x) for x in str(number)]

    armstrong = 0
    for num in number_list:
        num = num ** (len(number_list))
        armstrong += num
    if armstrong == number:
        print(f"Wow. {number} is an Armstrong number! The result is {True}.")
        return True
    else:
        print(
            "Well, doesn't look like {number} is an Armstrong number. {armstrong} is not equal to {number}."
        )
        return False


print(is_armstrong_number(153))
print(is_armstrong_number(9))
print(is_armstrong_number(27))
