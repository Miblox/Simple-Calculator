# Simple Calculator
import sys
import time
from logic import plusss, minusss, multiplicationn, divisionn, divisionnn, Degree, percent

# a = 0
# b = 0 

print("Welcome to the calculator! Press CTRL+C to close the program.")
# Сама программа

while True:

    try:

        choice_input = input("Choose the operation to perform: +, -, *, //, /, **, %.  ").strip()

# функции в logic.py для изменения кода исопльзуете этот файл

        operations = {
            "+": plusss,
            "-": minusss,
            "*": multiplicationn,
            "/": divisionnn,
            "//": divisionn,
            "**": Degree,
            "%": percent
        }

        if choice_input in operations:
            operations[choice_input]()

        else:
            print("This item is not in the calculator's database, or support for it has not been added.")


    except KeyboardInterrupt:
        print("\nExiting...")
        time.sleep(3)
        sys.exit()