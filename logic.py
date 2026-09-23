def plusss():
    a = 0
    b = 0
    while True:
        try:
            user_input = int(input("Введите число 1:  "))
        except ValueError:
            print("Веедены направильные данные введите ЧИСЛО!")
            continue

        a += user_input

        try:
            user_input22 = int(input("Введите число 2: "))
        except ValueError:
            print("введены неверные данные!")
            continue

        b += user_input22

        pluss = a + b
        print(f"Ответ равен {pluss}")
        return

def minusss():
    a = 0
    b = 0
    while True:
        try:
            user_input3 = int(input("Введите число 1: "))
        except ValueError:
            print("Введены неверные данные!")
            continue
        a += user_input3
        try:
            user_input4 = int(input("Введите число 2: "))
        except ValueError:
            print("Введены неверные данные!")
            continue

        b += user_input4
        minuss = a - b
        print(f"Ответ равен {minuss}")
        return

def multiplicationn():
    a = 0
    b = 0 
    while True:
        try:
            user_input5 = int(input("Введите число 1: "))
        except ValueError:
            print("Введены неверные данные!")
            continue
        a += user_input5
        try:
            user_input6 = int(input("Введите число 2: "))
        except ValueError:
            print("Введены неверные данные!")
            continue

        b += user_input6
        answer = a * b
        print(f"Ответ: {answer}")    
        return

def divisionn():
    a = 0
    b = 0
    while True:
        try:
            user_input7 = int(input("Введите число 1: "))
        except ValueError:
            print("Введены неверные данные!")
            continue
        a += user_input7
        try:
            user_input8 = int(input("Введите число 2: "))
        except ValueError:
            print("Введены неверные данные!")
            continue

        b += user_input8
        try:
            answer = a // b
        except ZeroDivisionError:
            print("На ноль делить нельзя")
            return
        print(f"Ответ: {answer}")    
        return   