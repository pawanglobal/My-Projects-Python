class Dog:
    """ Every dog's description."""
    def __init__(self, name, age, born):
        """initializing age and name attributes."""
        #attributes
        self.name = name
        self.age = age
        self.born = born
        #setting default value for attribute
        self.tail = 1


    # methods
    def sit(self):
        """simulate a dog sitting in response to command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """simulate a dog to roll over in response to a command"""
        print(f"{self.name} is now rolling")

    # updating tail's value through method
    def update_tail(self, dog_tail):
        """ dog tail is the new value for dog's tail"""
        self.tail = dog_tail

# instances
my_dog = Dog('willie', 3, '20 october 2000.')
print(f"{my_dog.name.title()} is my dog's name, and has {my_dog.tail} long tail.")
print(f"My dog is {my_dog.age} years old, and he was born on {my_dog.born}")
my_dog.sit()
my_dog.roll_over

# modifying attribute's value directly
my_dog.tail = '1/2'
print(f"Now my dog has {my_dog.tail} tail.")

#modifying value through function
my_dog.update_tail('no')
print(f"My dog has {my_dog.tail} tail.")
