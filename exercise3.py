def is_even(my_number):
    if abs(my_number) % 2 == 0:
        return True
    elif abs(my_number) % 2 == 1:
        return False
    else:
        return "This number is 0."
print(is_even(20))
print(is_even(-20))
print(is_even(0))
print(is_even(31))
print(is_even(-31))