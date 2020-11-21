#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""BasicCalculator is a terminal calculator"""

__author__ = "CBTMaster420 also known as soppyMann"
__version__ = "0.1"

operators = ["+", "-", "*", "/", "^"]
result = 0




while True:
    try:
        num1 = int(input("Type in a number:"))
    except:
        print("That is not a whole number!")
    else:
        break


while True:
    try:
        num2 = int(input("Now type in another number:"))
    except:
        print("That is not a whole number!")
    else:
        break


while True:
    operator = input("Now type in an operator(+, *, ^, / or -): ")
    if operator not in operators:
        print("That is not a recognized operator!")
    elif num2 == int(0) and operator in "/":
        print("You cannot divide by zero!")
        continue
    else:
        break


while result == 0:
    if operator == operators[0]:
        result = num1 + num2
        print("The result is:", result)
        break
    elif operator == operators[1]:
        result = num1 - num2
        print("The result is:", result)
        break
    elif operator == operators[2]:
        result = num1 * num2
        print("The result is:", result)
        break
    elif operator == operators[3]:
        result = num1 / num2
        if result.is_integer():
            print("The result is:", int(result))
        else:
            print("The result is:", result)
        break
    elif operator == operators[4]:
        result = num1 ** num2
        print("The result is:", result)
        break
