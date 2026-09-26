# Instance attributes
#
# Attributes belonging to individual objects are called instance attributes.
#
# class Student:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# Create two students:
#
# student1 = Student("Ajay", 21)
# student2 = Student("ram", 22)

# Give objects behavior with instance methods
#
# An object should generally do more than store data.
#
# For example:
#
# class Student:
#
#     def __init__(self, name, progress):
#         self.name = name
#         self.progress = progress
#
#     def update_progress(self, amount):
#         self.progress += amount
#
# Usage:
#
# student = Student("Ajay", 50)
#
# student.update_progress(10)
#
# print(student.progress)

# Methods can protect an object's state
#
# Suppose progress should never become negative or exceed 100.
#
# Instead of allowing unrestricted modification:
#
# student.progress += 1000
#
# we can make the object's behavior enforce the rules:
#
# class Student:
#
#     def __init__(self, name, progress=0):
#         self.name = name
#         self.progress = progress
#
#     def update_progress(self, amount):
#         if amount < 0:
#             raise ValueError("Progress cannot decrease.")
#
#         self.progress += amount
#
#         if self.progress > 100:
#             self.progress = 100
#
# The object now has some control over how its state changes.

# Instance method vs ordinary function
#
# Compare these two approaches:
#
# def calculate_progress(progress, amount):
#     return progress + amount
#
# and:
#
# class Student:
#
#     def update_progress(self, amount):
#         self.progress += amount
#
# The first approach explicitly receives the required data and returns a result.
#
# The second associates the behavior with an object that already owns the relevant state.

# Class attributes
#
# Not every piece of information needs to be stored separately inside every object.
#
# Consider:
#
# class Student:
#
#     university = "MAKAUT"
#
#     def __init__(self, name):
#         self.name = name
#
# Here, university is a class attribute.
#
# Both instances can access it:
#
# student1 = Student("Ajay")
# student2 = Student("siya")
#
# print(student1.university)
# print(student2.university)

# How attribute lookup works
#
# There's an important Python detail behind this.
#
# Suppose:
#
# class Student:
#     university = "MAKAUT"
#
#     def __init__(self, name):
#         self.name = name
#
# When Python evaluates:
#
# student.university
#
# it looks for the attribute associated with the instance and, if it isn't found there, continues the lookup through the class.
#
# You can inspect an instance's namespace with:
#
# print(student.__dict__)
#
# You might see:
#
# {'name': 'Ajay'}
#
# university doesn't have to be physically stored in that instance.

#Class methods
# class Student:
#     university = "makaut"
#     @classmethod
#     def get_uni(cls):
#         return cls.university
# print(Student.get_uni())

# A practical use of class methods: alternative constructors
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def from_string(cls,data):
#         name, age = data.split(",")
#         return cls(name,int(age))
#
# student = Student.from_string("Deep,21")
# print(student.name)

# # Static methods
# class Student:
#     @staticmethod
#     def is_valid_age(age):
#         return 18 <= age <=100
# print(Student.is_valid_age(58))

# Protected convention: _name
#
# Python doesn't have a traditional protected keyword.
#
# Instead:
#
# self._balance
#
# means:
#
# This is an internal implementation detail; external code generally shouldn't access it directly.
#
# Example:
#
# class BankAccount:
#
#     def __init__(self, balance):
#         self._balance = balance
#
# The underscore is a convention, not a security mechanism.

# Private convention: __name
#
# Double leading underscore triggers name mangling.
#
# class BankAccount:
#
#     def __init__(self, balance):
#         self.__balance = balance
#
# Now:
#
# account.__balance
#
# doesn't directly work as you might expect.
#
# Python internally transforms the name approximately into:
#
# _BankAccount__balance
#
# You can technically access it:
#
# account._BankAccount__balance
#
# but that's not the intended interface.

# Why properties?
#
# Suppose we have:
#
# class BankAccount:
#
#     def __init__(self, balance):
#         self._balance = balance
#
# We want external code to be able to do:
#
# print(account.balance)
#
# but internally we want:
#
# _balance
#
# and controlled access.
#
# Python provides:
#
# @property
#
# Basic @property
# class BankAccount:
#
#     def __init__(self, balance):
#         self._balance = balance
#     @property
#     def balance(self):
#         return self._balance

# Now:
# account = BankAccount(5000)
# print(account.balance)
# Notice:
# account.balance
# not:
# account.balance()
# Even though balance is implemented using a method.

# Property getter
#
# This:
#
# @property
# def balance(self):
#     return self._balance
# is called a getter.
# It lets you expose controlled read access.
#
# Conceptually:
# account.balance
#       ↓
# @property getter
#       ↓
# self._balance

# Property setter
# What if we want controlled modification?
# class BankAccount:
#
#     def __init__(self, balance):
#         self.balance = balance
#     @property
#     def balance(self):
#         return self._balance
#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             raise ValueError("Balance cannot be negative")
#
#         self._balance = value
#
# Now:
# account = BankAccount(5000)
# works.
# But:
# account.balance = -100
# raises:
# ValueError
# The assignment:
# account.balance = 7000
# automatically invokes:
# @balance.setter

# Computed properties
# Properties don't have to simply return a stored value.
# Example:
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     @property
#     def area(self):
#         return self.width * self.height
#
# Usage:
# rectangle = Rectangle(10, 5)
# print(rectangle.area)

# Property deleter
# Python also allows:
# @property
# def value(self):
#     ...
# @value.deleter
# def value(self):
#     ...
#
# Example:
# class User:
#
#     def __init__(self, name):
#         self._name = name
#     @property
#     def name(self):
#         return self._name
#     @name.deleter
#     def name(self):
#         del self._name
#
# Then:
# del user.name
# invokes the deleter.