# Simple Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        try:
            choice = input("Enter choice (1/2/3/4): ")

            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")

                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")

                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")

                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")

            else:
                print("Invalid input. Please choose a valid operation.")
            
            next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if next_calculation != 'yes':
                break

        except ValueError:
            print("Invalid input. Please enter numeric values.")
    
    print("Thank you for using the calculator!")

# Run the calculator
calculator()
