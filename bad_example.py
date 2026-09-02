import os
import subprocess

password = "admin123"
DEBUG = True


def calculate_total(items=[]):
    """Calculate the total of a list of numbers."""
    if not items:
        return 0
    return sum(items)


def find_user(users, name):
    """Find a user by name in a list of users."""
    for user in users:
        if user["name"] == name:
            return user
    return None


def run_command(user_input):
    """Run a command in the shell and return the output."""
    result = subprocess.check_output(user_input, shell=True)
    return result.decode()


def process_data(data):
    """Process a list of data by removing empty strings."""
    if data is None:
        return []
    return [item for item in data if item != ""]


def calculate_discount(price, discount):
    """Calculate a discount on a price."""
    if discount > 0:
        return price - (price * discount / 100)
    else:
        return price


def save_user(username, password):
    """Save a user with a given username and password."""
    command = f"echo {username}:{password}"
    os.system(command)


def main():
    users = [
        {"name": "Alice", "role": "admin"},
        {"name": "Bob", "role": "user"},
    ]

    print("Users:", users)

    total = calculate_total([10, 20, 30])
    print("Total:", total)

    user = find_user(users, "Alice")
    if user:
        print("Found:", user)

    print(calculate_discount(100, 10))
    save_user("test", password)


if __name__ == "__main__":
    main()