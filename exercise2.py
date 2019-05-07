def negative(my_number):
    if my_number < 0:
        return True
    elif my_number > 0:
        return False
    else:
        return "This number is 0."
print(negative(1))
print(negative(0))
print(negative(-1))