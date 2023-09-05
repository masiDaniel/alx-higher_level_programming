#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
if num < 0:
	digit = -digit
print("Last digit of {} is {} and is " .format(num, digit), end = "")
if digit > 5:
	print("greater then 5")
elif digit == 0:
	print("0")
else:
	print("less than 6 not 0")
