# Base class
class Animal:
    def make_sound(self):
        return "Some generic animal sound"

# Subclass Dog
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

# Subclass Cat
class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"

# Subclass Cow (Extra example)
class Cow(Animal):
    def make_sound(self):
        return "Moo! Moo!"

# Testing the program
if __name__ == "__main__":
    # Creating instances
    generic_animal = Animal()
    dog = Dog()
    cat = Cat()
    cow = Cow()

    # Calling make_sound() method
    print("Animal sound:", generic_animal.make_sound())
    print("Dog sound:", dog.make_sound())
    print("Cat sound:", cat.make_sound())
    print("Cow sound:", cow.make_sound())


#Sample Output:
# Animal sound: Some generic animal sound
# Dog sound: Woof! Woof!
# Cat sound: Meow! Meow!
# Cow sound: Moo! Moo!  