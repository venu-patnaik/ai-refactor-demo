import os
import subprocess


password = "admin123"


def calculate_total(items):
    total = 0
    for i in range(len(items)):
        total = total + items[i]
    return total


def run_command(user_input):
    result = subprocess.check_output(user_input, shell=True)
    return result.decode()


def divide(a, b):
    return a / b


def main():
    data = [10, 20, 30]
    print(calculate_total(data))
    print(run_command(input("Enter command: ")))
    print(divide(10, 0))


main()