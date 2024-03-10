def addition():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = a + b
    print("The result of addition is", c)

def subtraction():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = a - b
    print("The result of subtraction is", c)

def multiply():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = a * b
    print("The result of multiplication is", c)

def divide():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    if b != 0:
        c = a / b
        print("The result of division is", c)
    else:
        print("Error: Division by zero!")

while True:
    print("1- Addition")
    print("2- Subtraction")
    print("3- Multiplication")
    print("4- Division")
    print("5- Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        addition()
    elif choice == '2':
        subtraction()
    elif choice == '3':
        multiply()
    elif choice == '4':
        divide()
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a valid option.")


