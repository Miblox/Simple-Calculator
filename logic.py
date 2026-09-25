def plusss():
    while True:
        try:
            a = int(input("Enter the number 1:  "))
        except ValueError:
            print("Invalid data has been entered!")
            continue

        

        try:
            b = int(input("Enter the number 2: "))
        except ValueError:
            print("Invalid data has been entered!")
            continue

        

        pluss = a + b
        print(f"The answer equals  {pluss}")
        return

def minusss():
    while True:
        try:
            a = int(input("Enter the number 1: "))
        except ValueError:
            print("Invalid data has been entered!")
            continue
        
        try:
            b = int(input("Enter the number 2: "))
        except ValueError:
            print("Invalid data has been entered!")
            continue

        
        minuss = a - b
        print(f"The answer equals  {minuss}")
        return

def multiplicationn(): 
    while True:
        try:
            a = int(input("Enter the number 1: "))
        except ValueError:
            print("Invalid data has been entered!")
            continue
        
        try:
            b = int(input("Enter the number 2: "))
        except ValueError:
            print("Invalid data has been entered!")
            continue

        
        answer = a * b
        print(f"The answer equals : {answer}")    
        return

def divisionn():
    while True:
        try:
            a = int(input("Enter the number 1: "))
        except ValueError:
            print("Invalid data has been entered!")
            continue
        
        try:
            b = int(input("Enter the number 2: "))
        except ValueError:
            print("Invalid data has been entered!")
            continue

        
        try:
            answer = a // b
        except ZeroDivisionError:
            print("You can't divide by zero.")
            return
        print(f"The answer equals : {answer}")    
        return  

def divisionnn():
    while True:
        try:
            a = int(input("Enter the number 1: "))
        except ValueError:
            print("Invalid data has been entered!")
            continue
        
        try:
            b = int(input("Enter the number 2: "))
        except ValueError:
            print("Invalid data has been entered!")
            continue

        
        try:
            answer = a / b
        except ZeroDivisionError:
            print("You can't divide by zero.")
            return
        print(f"The answer equals : {answer}")    
        return

def Degree():
    while True:
        try:
            a = int(input("Enter the number 1: "))
        except ValueError:
            print("Invalid data has been entered!")
            continue
        
        try:
            b = int(input("Enter the number 2: "))
        except ValueError:
            print("Invalid data has been entered!")
            continue

        try:
            answer = a ** b  
        except ZeroDivisionError:
            print("You cannot raise zero to a negative power")
            return
        
        print(f"The answer equals : {answer}") 

        return


