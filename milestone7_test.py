import os
import subprocess


password = "admin123"


def calculate_total(items):
    """Calculate the total of a list of numbers."""
    return sum(items)


def run_command(user_input):
    """Run a command and return its output as a string."""
    try:
        result = subprocess.check_output(user_input, shell=True).decode()
        return result
    except Exception as e:
        print(f'An error occurred: {e}')
        raise


def divide(a, b):
    """Divide two numbers and return the result."""
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b


def get_user_input():
    """Get user input from the console."""
    return input("Enter command: ")


def main():
    data = [10, 20, 30]
    print(calculate_total(data))
    try:
        print(run_command(get_user_input()))
    except Exception as e:
        print(f'An error occurred: {e}')
    try:
        print(divide(10, 0))
    except ValueError as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()