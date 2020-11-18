try:
    num1 = int(input("Type in a number:"))
    num2 = int(input("Now type in another number:"))
except:
    print("That is not a number!")
    exit()

sym = (input("Now type in an operator(+, *, ^, / or -): "))

result = 0
if sym == "+":
    result = num1 + num2
    print("The result is:", result)
elif sym == "-":
    result = num1 - num2
    print("The result is:", result)
elif sym == "*":
    result = num1 * num2
    print("The result is:", result)
elif sym == "/":
    result = num1 / num2
    print("The result is:", result)
elif sym == "^":
    result = num1 ** num2
    print("The result is:", result)
else:
    print("The operator you introduced is not recognized!")
