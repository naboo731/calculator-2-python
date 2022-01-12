"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    calc_input = input('Enter the equation>>')
    tokens = calc_input.split(' ')

    if "q" in tokens:
        print('Exiting the calculator, goodbye!')
        break
    elif len(tokens) < 2:
        print('More inputs needed')

    operator = tokens[0]
    num1 = tokens[1]
    num2 = tokens[2]

    result = None
    if operator == '+':
        result = add(float(num1), float(num2))
    elif operator == '-':
        result = subtract(float(num1), float(num2))
    elif operator == '*':
        result = multiply(float(num1), float(num2))
    elif operator == '/':
        result = divide(float(num1), float(num2))
    elif operator == "sqr":
        result = square(float(num1))
    elif operator == "cube":
        result = cube(float(num1))
    elif operator == "pow":
        result = power(float(num1), float(num2))
    elif operator == "%":
        result = mod(float(num1), float(num2))
    else:
        print('Please enter an operator followed by one or two integers')
    print(result)
