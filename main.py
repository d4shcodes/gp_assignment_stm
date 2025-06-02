"""
Simple CLI Calculator App
Provides basic arithmetic operations: addition, subtraction, multiplication, division, exponentiation, and modulus.
Prepared by : sofea, amirah, dinesh raj & dashen
"""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is undefined."

def power(a, b):
    return a ** b


def modulus(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "Error: Modulus by zero is undefined."


def main():
    operations = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide),
        "5": ("Power", power),
        "6": ("Modulus", modulus)
    }

    print("Welcome to the Calculator App!")
    while True:
        print("\nSelect an operation:")
        for key, (name, _) in operations.items():
            print(f"  {key}. {name}")
        print("  q. Quit")

        choice = input("Enter choice: ").strip()
        if choice.lower() == 'q':
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        operation_name, operation_func = operations[choice]
        result = operation_func(num1, num2)
        print(f"Result of {operation_name}({num1}, {num2}) = {result}")


if __name__ == "__main__":
    main()
