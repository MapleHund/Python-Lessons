class Dog:
    # A simple attempt to model a dog

#     def __str__(self):
#         return 'woof'

    def __init__(self, name, age):
        # initialize name and attirbutes
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is sitting.')

    def roll_over(self):
        print(f'{self.name} rolled over.')


my_dog = Dog('Willie', 6)
your_dog = Dog('Lucie', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

print(my_dog) # what is this printing? Is it the memory address?

# just calling will return the string
my_dog.sit()
# Calling in a print() will first output the method result, then None value is printed
print(my_dog.roll_over())
print()

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
