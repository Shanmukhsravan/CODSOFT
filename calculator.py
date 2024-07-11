def add(a: float, b: float) :
    return a + b

def sub(a: float, b: float) :
    return a - b

def division(a: float, b: float) -> float:
    return a / b

def multiply(a: float, b: float) -> float:
    return a * b

def main():
    print("Enter two numbers:")
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    print("\t->Select The operation to perform<-\t\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", sub(num1, num2))
    elif choice == 3:
        print("Result:", multiply(num1, num2))
    elif choice == 4:
        print("Result:", division(num1, num2))
    else:
        print("Enter a valid operation!")

main()
