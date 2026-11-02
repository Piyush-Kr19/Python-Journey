# Python Calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the first number: "))


if operator == '+':
    result = num1 + num2
    print(result)
    pass
elif operator == '-':
    result = num1 - num2
    print(result)
    pass
elif operator == '*':
    result = num1 * num2
    print(result)
    pass
elif operator == '/':
    result = num1 / num2
    print(round(result,3))
    pass
else:
    print(f"{operator} is valid operator")
