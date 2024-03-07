# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

history = []  # List to store calculation history

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. History")
    print("6. Exit")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            print(num1, "+", num2, "=", result)

        elif choice == '2':
            result = subtract(num1, num2)
            print(num1, "-", num2, "=", result)

        elif choice == '3':
            result = multiply(num1, num2)
            print(num1, "*", num2, "=", result)

        elif choice == '4':
            result = divide(num1, num2)
            print(num1, "/", num2, "=", result)

        history.append((num1, num2, result))  # Add calculation to history

    elif choice == '5':
        if not history:
            print("History is empty.")
        else:
            print("Calculation History:")
            for calc in history:
                print(calc[0], "+", calc[1], "=", calc[2])

    elif choice == '6':
        break  # Exit the calculator

    else:
        print("Invalid input")