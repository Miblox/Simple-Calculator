def plusss():
    while True:
        try:
            a = int(input("Введите число 1:  "))
        except ValueError:
            print("Веедены направильные данные введите ЧИСЛО!")
            continue

        

        try:
            b = int(input("Введите число 2: "))
        except ValueError:
            print("введены неверные данные!")
            continue

        

        pluss = a + b
        print(f"Ответ равен {pluss}")
        return

def minusss():
    while True:
        try:
            a = int(input("Введите число 1: "))
        except ValueError:
            print("Введены неверные данные!")
            continue
        
        try:
            b = int(input("Введите число 2: "))
        except ValueError:
            print("Введены неверные данные!")
            continue

        
        minuss = a - b
        print(f"Ответ равен {minuss}")
        return

def multiplicationn(): 
    while True:
        try:
            a = int(input("Введите число 1: "))
        except ValueError:
            print("Введены неверные данные!")
            continue
        
        try:
            b = int(input("Введите число 2: "))
        except ValueError:
            print("Введены неверные данные!")
            continue

        
        answer = a * b
        print(f"Ответ: {answer}")    
        return

def divisionn():
    while True:
        try:
            a = int(input("Введите число 1: "))
        except ValueError:
            print("Введены неверные данные!")
            continue
        
        try:
            b = int(input("Введите число 2: "))
        except ValueError:
            print("Введены неверные данные!")
            continue

        
        try:
            answer = a // b
        except ZeroDivisionError:
            print("На ноль делить нельзя")
            return
        print(f"Ответ: {answer}")    
        return  

def divisionnn():
    while True:
        try:
            a = int(input("Введите число 1: "))
        except ValueError:
            print("Введены неверные данные!")
            continue
        
        try:
            b = int(input("Введите число 2: "))
        except ValueError:
            print("Введены неверные данные!")
            continue

        
        try:
            answer = a / b
        except ZeroDivisionError:
            print("На ноль делить нельзя")
            return
        print(f"Ответ: {answer}")    
        return
