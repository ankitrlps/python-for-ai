class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def eat(self, item):
        print(f"{self.name} is eating {item}.")
        
    def sleep(self):
        print(f"{self.name} is sleeping.")