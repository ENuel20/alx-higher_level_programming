#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = str(number)[-1]
last_dig = int(last_dig)
if last_digit == 0:
    print(f"last digit of {number} is {last_digit} and is 0")
elif last_digit <= 5 and last_digit != 0:
    print(f"last digit of {number} is {last_digit} and is less than 6 and not 0")
else:
    print(f"last digit of {number} is {last_digit} and is greater than 5")
