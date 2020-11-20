operators = ["+", "-", "*", "/", "^"]
result = 0


while True:
    try:
        num1 = int(input("Type in a number:"))
    except:
        print("That is not a number!")
    else:
        break

while True:
    try:
        num2 = int(input("Now type in another number:"))
    except:
        print("That is not a number!")
    else:
        break


while True:
    sym = input("Now type in an operator(+, *, ^, / or -): ")
    if sym not in operators:
        print("That is not a recognized operator!")
    elif num2 == int(0) and sym in "/":
        print("You cannot divide by zero!")
        continue
    else:
        break
    


while result == 0:
    if sym == operators[0]:
        result = num1 + num2
        print("The result is:", result)
    elif sym == operators[1]:
        result = num1 - num2
        print("The result is:", result)
    elif sym == operators[2]:
        result = num1 * num2
        print("The result is:", result)
        break
    elif sym == operators[3]:
        result = num1 / num2
        print("The result is:", result)
    elif sym == operators[4]:
        result = num1 ** num2
        print("The result is:", result)
