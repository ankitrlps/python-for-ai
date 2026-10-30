class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print(f"{self.name} barks: Woof!")
        
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
teddy = Dog(name="Teddy", breed="Cavapoo")
teddy.bark()  # Output: Teddy barks: Woof!
teddy1 = Dog("Teddy1", "Cavapoo1")

print(teddy.name)  # Output: Teddy
print(teddy.breed)  # Output: Cavapoo
print(teddy1.name)  # Output: Teddy
print(teddy1.breed)  # Output: Cavapoo

