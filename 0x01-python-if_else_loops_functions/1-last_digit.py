#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    i = -1 * number
else:
    i = number
while i > 9:
    i %= 10
if i > 5 and number > 0:
    print("Last digit of {} is {} and is greater than 5".format(number, i))
elif i == 0:
    print("Last digit of {} is {} and is 0".format(number, i))
else:
    if number > 0:
        print("Last digit of {} is {} and is less than 6 and not \
0".format(number, i))
    else:
        print("Last digit of {} is -{} and is less than 6 and not \
0".format(number, i))
