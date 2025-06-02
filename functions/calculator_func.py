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
