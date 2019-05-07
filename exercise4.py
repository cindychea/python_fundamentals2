def eight_or_less(my_string):
    if len(my_string) <= 8:
        return True
    else:
        return False
print(eight_or_less('cats'))
print(eight_or_less('cats are rad'))
print(eight_or_less('myturtle'))
