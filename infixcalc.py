#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$infixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em `infixcalc.log`
"""
__version__ = "0.1.0"
__author__ = "Rafael Freitas"
__license__ = "Unlicense"

import sys
import os

from datetime import datetime
arguments = sys.argv[1:]


valid_operations = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a // b,
}

#valid_operations = ("sum", "sub", "mul", "div")

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
user = os.getenv("USER","anonymous")

while True:

    #Validation
    if not arguments:
        operation = input("Choose the operation (sum, sub, mul, div): ")
        n1 = input("Input the first number: ")
        n2 = input("Input the second number: ")
        arguments = [operation, n1, n2]
    elif len(arguments) != 3:
        print("Number of arguments invalid")
        print("ex: `um 5 5`")
        sys.exit(1)

    operation, *nums = arguments
    print(f"{nums=}, {operation=}")

    if operation not in valid_operations:
        print("Operation invalid")
        print(f"Acceptable values for operation: {valid_operations.keys()}")

    validated_nums = []
    for num in nums:
        if not num.replace(".", "").isdigit():
            print(f"Invalid number {num}")
            sys.exit(2)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num)
    try:
        n1, n2 = validated_nums
    except ValueError as e:
        print(f"[ERROR] {str(e)}")
        sys.exit(1)

    # TODO: Usar dict de funções
    result = valid_operations[operation](n1,n2)

    # if operation == "sum":
    #     result = n1 + n2
    # elif operation == "sub":
    #     result = n1 - n2
    # elif operation == "mul":
    #     result = n1 * n2
    # elif operation == "div":
    #     result = n1 / n2

    print(f"O resultado da operação é {result}")

    try:
        with open(filepath, "a") as log:
            log.write(f"Date: {datetime.now().isoformat()} / User: {user} / Operation: {operation} / params: {n1}, {n2} / result: {result}\n")
    except PermissionError as e:
        print(f"[ERROR] {str(e)}")
        sys.exit(1)

    arguments = None

    if input("Press enter to continue or any key to exit"):
        break

# Minha solução
# if args:
#     arguments["operation"] = args[0]
#     arguments["number_one"] = int(args[1])
#     arguments["number_two"] = int(args[2])
# else:
#     arguments["operation"] = input("Choose the operation (sum, sub, mul, div): ")
#     arguments["number_one"] = int(input("Input the first number: "))
#     arguments["number_two"] = int(input("Input the second number: "))
#
#
# print(f"{arguments=}")
#
# if arguments["operation"] == "sum":
#     print(arguments["number_one"] + arguments["number_two"])
# elif arguments["operation"]  == "sub":
#     print(arguments["number_one"] - arguments["number_two"])
# elif arguments["operation"] == "mul":
#     print(arguments["number_one"] * arguments["number_two"])
# elif arguments["operation"] == "div":
#     print(arguments["number_one"] / arguments["number_two"])
# else:
#     print("Invalid operation !!!")


