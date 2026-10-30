from classes.animals.animal import Animal

class Dog(Animal):
    
    def bark(self):
        print(f"{self.name} barks: Woof!")
        
    # Overriding
    def eat(self, item):
        print(f"{self.name} is eating {item} with excitement!")