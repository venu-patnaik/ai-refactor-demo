import subprocess

def calculate_total(items):
    total = sum(items)
    return total

def run_command(user_input):
    try:
        result = subprocess.check_output(user_input, shell=False).decode()
        return result
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

def divide(numerator, denominator):
    if denominator == 0:
        raise ValueError('Cannot divide by zero')
    return numerator / denominator

def main():
    data = [10, 20, 30]
    print(calculate_total(data))
    user_input = input("Enter command: ")
    print(run_command(user_input))
    try:
        print(divide(10, 0))
    except ValueError as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
