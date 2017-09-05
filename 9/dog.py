class Dog():
    """A trial try to mock the dog"""

    def __init__(self, name, age):
        """init the attribute of name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """mock the dog sit action"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self, extra_attr):
        """mock the dog roll_over action"""
        print(self.name.title() + " rolled over!")
        print("Input the extra attr: " + extra_attr)


my_dog = Dog('willie', 6)
your_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.roll_over('Beat it')

if my_dog == your_dog:
    print("Great!")
