import os
import subprocess


password = "admin123"


def calculate_total(items):
    total = 0
    for item in items:  # Renamed 'i' to 'item' for clarity
        total += item  # Simplified the addition
    return total


def run_command(user_input):
    try:
        result = subprocess.check_output(user_input, shell=True)
        return result.decode()
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    data = [10, 20, 30]
    print(calculate_total(data))
    print(run_command(input("Enter command: ")))
    try:
        print(divide(10, 0))  # Wrapped the division in a try-except block
    except ValueError as e:
        print(e)  # Handle the division by zero error


main()