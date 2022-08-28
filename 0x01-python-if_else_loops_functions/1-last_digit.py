#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
l_digit = (number % 10)
varStr1 = "and is greater than 5"
varStr2 = "and is 0"
varStr3 = "and is less than 6 and not 0"
print("Last digit of", end=" ")
if (l_digit > 5):
    print("{} is {} {}".format(number, l_digit, varStr1))
elif (l_digit == 0):
    print("{} is {} {}".format(number, l_digit, varStr2))
elif (number < 0):
    print("{} is {} {}".format(number, (number * -1) % 10, varStr3))
else:
    print("{} is {} {}" .format(number, l_digit, varStr3))
