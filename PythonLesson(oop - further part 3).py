# *What is MRO?
# MRO = Method Resolution Order
# It tells Python:
# "When I ask for an attribute or method, which class should Python search first, second, third...?"
# Example:
# class A:
#     def show(self):
#         print("A")
#
# class B(A):
#     pass
#
# class C(B):
#     pass
#
# When:
# obj = C()
# obj.show()
#
# *Python searches approximately:
# C
# ↓
# B
# ↓
# A
# ↓
# object
#
# You can inspect it:
# print(C.mro())
#
# or:
#
# print(C.__mro__)
# You'll see something similar to:
#
# [
#     <class 'C'>,
#     <class 'B'>,
#     <class 'A'>,
#     <class 'object'>
# ]

# MRO with Multiple Inheritance
# Consider:
# class A:
#     def show(self):
#         print("A")

# class B(A):
#     pass
#
# class C(A):
#     pass
#
# class D(B, C):
#     pass
#
# The inheritance structure is:
#        A
#       / \
#      B   C
#       \ /
#        D
# Now:
# print(D.mro())

# *The Diamond Problem
#
# This structure is called the diamond inheritance problem:
#         A
#        / \
#       B   C
#        \ /
#         D
# Now suppose every class defines process():
# class A:
#     def process(self):
#         print("A")
#
# class B(A):
#     def process(self):
#         print("B")
#         super().process()
#
# class C(A):
#     def process(self):
#         print("C")
#         super().process()
#
# class D(B, C):
#     def process(self):
#         print("D")
#         super().process()
#
# Now:
# obj = D()
# obj.process()
#
# Output:
#
# D
# B
# C
# A
#
# Why?
# Because:
#
# print(D.mro())
#
# gives:
#
# D
# B
# C
# A
# object
#
# And every super() continues to the next class in the MRO.

# *Very Important: super() Does NOT Simply Mean "My Parent"
#
# This is one of the most important OOP concepts in Python.
#
# Many beginners think:
#
# super().process()
#
# means:
#
# Call my parent class's process().
#
# That's not quite correct.
#
# More accurately:
#
# super() delegates to the next class in the MRO.
#
# For:
#
# D → B → C → A → object
#
# when D executes:
#
# super().process()
#
# it goes to:
#
# B
#
# Then B's:
# super().process()
# goes to:
#
# C
#
# Then C's:
#
# super().process()
#
# goes to:
#
# A
#
# So:
#
# D
#  ↓ super()
# B
#  ↓ super()
# C
#  ↓ super()
# A
#
# *This is called cooperative multiple inheritance.

# *Practical Industry Pattern: Mixins
# Multiple inheritance is most useful when used for mixins.
#
# A mixin usually provides one focused behavior.
# Example:
#
# class LoggingMixin:
#
#     def log(self, message):
#         print(f"[LOG] {message}")
#
# class ValidationMixin:
#
#     def validate(self, data):
#         if not data:
#             raise ValueError("Data cannot be empty")
#
#         return True
#
# class UserService(LoggingMixin, ValidationMixin):
#
#     def create_user(self, data):
#         self.validate(data)
#         self.log("Creating user")
#         print("User created")
#
# Usage:
# service = UserService()
#
# service.create_user({
#     "name": "Deep",
#     "email": "deep@example.com"
# })
#
# The service receives:
# LoggingMixin
#       +
# ValidationMixin
#       ↓
#  UserService
# This is a much more reasonable use of multiple inheritance than creating complicated parent-child business hierarchies.
