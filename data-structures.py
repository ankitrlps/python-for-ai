
# List
age = 20
list = [1, 2, 3, 4, 5, "Hello", True, 3.14, age]
print(list[0])
list.append("New Item")
list.remove(list[-2]) # Remove the second last item from the list

print(len(list))


# Disctionary
person = {
    "name": "John Doe",
    "age": 30
}
print(person["name"])
person["age"] = 31

print(person.get("age"))
print(person.keys())
print(person.values())


# Tuples
empty = ()
coordinates = (10.0, 20.0)
colors = ("red", "green", "blue")

print(colors[0])
colors[0] = "yellow"

# Sets
empty_set = set()
fruits = {"apple", "banana", "orange"}
numbers = set([1, 2, 3, 4, 5])

# list to set
list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
set_from_list = set(list)