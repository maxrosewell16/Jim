print("Hello! This is a simple calculator program.")
choice = input("Choose an operation (+ or -): ")
if choice in ('+', '-'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
else:
    print("Invalid input. Please choose either + or -.")