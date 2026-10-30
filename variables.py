"""
This is a simple Python script that defines two variables: `name` and `age`. The variable `name` is initially set to "John Doe" and then updated to "Jane Smith". The variable `age` is set to 30.
"""

name = "John Doe"
age = 30

name = "Jane Smith"

result = 34 + 2 + age


def calculator(x, y, operation):
    if operation == "add":
        return x + y
    elif operation == "substract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
    
result = calculator(10, 5, "divide")


exist = True
exist = False

age = 20
can_vote = age >= 34

string = f"Hello, World! {age}".upper()