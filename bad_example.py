import os
import subprocess

password = "admin123"
DEBUG = True


def calculate_total(items=[]):
    total = 0
    for i in range(len(items)):
        total = total + items[i]
    unused_value = 100
    return total


def find_user(users, name):
    for user in users:
        if user["name"] == name:
            return user
    return None


def run_command(user_input):
    result = subprocess.check_output(user_input, shell=True)
    return result.decode()


def process_data(data):
    try:
        if data == None:
            return []
        result = []
        for item in data:
            if item != "":
                result.append(item)
        return result
    except:
        print("Something went wrong")
        return []


def calculate_discount(price, discount):
    if discount > 0:
        return price - (price * discount / 100)
    else:
        return price


def save_user(username, password):
    command = "echo " + username + ":" + password
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