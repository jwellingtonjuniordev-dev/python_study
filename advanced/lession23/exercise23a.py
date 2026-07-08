# Exercise 23a.1
# Create:
# class Person
#
# Implement:
# __new__()
# Print:
# Creating Person...
#
# Implement:
# __init__()
# Print:
# Initializing Person...
#
# Create one object.

class Person:
    def __new__(cls):
        print("Creating Person...")
        return super().__new__(cls)
    
    def __init__(self):
        print("Initializing Person...")

person = Person()

# Exercise 23a.2
# Create:
# class Car
#
# __new__()
# Print:
# Building the car...
#
# __init__()
# Print:
# Painting the car...
#
# Create one object.

class Car:
    def __new__(cls):
        print("Building the car...")
        return super().__new__(cls)
    
    def __init__(self):
        print("Painting the car...")

car = Car()

# Mini Challenge
# Create:
# class Animal
#
# __new__()
# Print:
# Animal __new__
#
# __init__()
# Print:
# Animal __init__
#
# Create:
# class Dog(Animal)
#
# __new__()
# Print:
# Dog __new__
#
# Call:
# super().__new__(cls)
#
# __init__()
# Print:
# Dog __init__
#
# Call:
# super().__init__()
#
# Create:
#
# dog = Dog()
#
# Without executing,
# try to predict the output.

class Animal:
    def __new__(cls):
        print("Animal __new__")
        return super().__new__(cls)
    
    def __init__(self):
        print("Animal __init__")

class Dog(Animal):
    def __new__(cls):
        print("Dog __new__")
        return super().__new__(cls)
    
    def __init__(self):
        print("Dog __init__")
        super().__init__()

# the output will be:
# Dog __new__
# Animal __new__
# Dog __init__
# Animal __init__

