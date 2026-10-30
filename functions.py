def my_function(first_name="John", last_name="Doe"):
    print(first_name + " " + last_name)
    
my_function("Ankit")

my_function(last_name="Ankit", first_name="Renduchintala")


# function that takes an arbitrary number of arguments
def my_function1(*kids):
    print("The youngest child is " + kids[2])
    
my_function1("Emil", "Tobias", "xyz", "Linus")

# function that takes an arbitrary number of keyword arguments
def my_function2(**kwargs):
    print("His last name is " + kwargs["lname"])

my_function2(fname="Tobias", lname="Refsnes")

# function that returns multiple values
def my_function3():
    numbers = [1, 2, 3, 4, 5]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number

first_number = my_function3()
first_number, last_number = my_function3()
f, s = my_function3()
print(f, s)