def calculate(x,y):
    print("Starting calculation")
    if x==0:
        return 0
    elif x<0:
        return x+y
    else:
        result=0
        for i in range(y):
            result=result+x
        return result

password="admin123"

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b


def hello():
    print("hello")
    return "Hello World!"

# Add blank lines after class or function definitions to improve readability

# Consider using more descriptive variable names, such as 'password_string' instead of 'password'

# Use type hints for function parameters and return types to improve code readability and maintainability
