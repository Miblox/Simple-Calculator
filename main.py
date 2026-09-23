# Simple Calculator
import sys
import time
from logic import plusss, minusss, multiplicationn, divisionn

a = 0
b = 0

print("Добро пожаловать в калькулятор! нажмите CTRL+C чтобы закрыть программу")
# Сама программа

while True:

    try:

        choicee = ["+", "-", "*", ":"]
        choice_input = input("Выбери что надо сделать: +, -, *, :,  ")

# функции в logic.py для изменения кода исопльзуете этот файл

        if choice_input == "+":
            plusss()

        elif choice_input == "-":
            minusss()

        elif choice_input == "*":
            multiplicationn()

        elif choice_input == ":":
            divisionn()

        else:
            print("В базе калькулятора нет такого или поддержка не добавлена")


    except KeyboardInterrupt:
        print("\n Выходим...")
        time.sleep(3)
        sys.exit()



# while True:
#    try:
#        user_input = int(input("Введите число 1:  "))
#    except ValueError:
#        print("Веедены направильные данные введите ЧИСЛО!")
#        continue
#
#   a += user_input
#
#    try:
#        user_input22 = int(input("Введите число 2: "))
#    except ValueError:
#        print("введены неверные данные!")
#        continue
#
#    b += user_input22
#
#    pluss = a + b
#    print(f"Ответ равен {pluss}")




# 67 SIX SEVEN!!