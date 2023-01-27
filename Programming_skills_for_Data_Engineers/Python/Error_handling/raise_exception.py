import os

print(os.getcwd())

list_x = [-5, -3, 0, 9, 4]
numbers = range(-5, 10)

for number in numbers:
    print(f"current number is {number}")
    if number not in list_x:
        # This is a raising for exception without handeling it
        raise Exception(f"Number {number} is not accepted")
