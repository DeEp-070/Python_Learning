# *Basic inheritance
# class Payment:
#
#     def process(self):
#         print("Processing payment")
#
#
# class CardPayment(Payment):
#     pass
#
# Now:
#
# payment = CardPayment()
#
# payment.process()

# *Child-specific attributes
# Suppose card payments need:
# card_last_four
# Then:
#
# class CardPayment(Payment):
#
#     def __init__(self, payment_id, amount, card_last_four):
#         self.payment_id = payment_id
#         self.amount = amount
#         self.card_last_four = card_last_four
#
# This works, but there is duplication:
# self.payment_id = payment_id
# self.amount = amount
# We don't want to duplicate the parent's initialization logic.
# That's where super() comes in.

# super()
# Use:
# class CardPayment(Payment):
#
#     def __init__(self, payment_id, amount, card_last_four):
#         super().__init__(payment_id, amount)
#         self.card_last_four = card_last_four
#
# Now:
# payment = CardPayment(
#     "PAY-101",
#     5000,
#     "1234"
# )
#
# *The flow is:
# CardPayment.__init__()
#         │
#         ├── super().__init__()
#         │        ↓
#         │   Payment.__init__()
#         │        ↓
#         │   payment_id
#         │   amount
#         │
#         └── card_last_four
# This is much cleaner.

# *Why super() is better than explicitly naming the parent
#
# You could write:
#
# Payment.__init__(self, payment_id, amount)
# but generally prefer:
# super().__init__(payment_id, amount)
# because super() participates in Python's method resolution order (MRO).

# *Method overriding
# A child class can provide its own implementation of a method inherited from the parent.
#
# class Payment:
#     def process(self):
#         print("Processing generic payment")
#
# class CardPayment(Payment):
#     def process(self):
#         print("Processing card payment")
#
# Now:
# payment = CardPayment()
# payment.process()
#
# outputs:
# Processing card payment
# The child implementation overrides the inherited implementation.

# *super() with overridden methods
# You can also extend the parent's behavior rather than completely replacing it.
#
# class Payment:
#
#     def process(self):
#         print("Validating payment")
#
#
# class CardPayment(Payment):
#
#     def process(self):
#         super().process()
#         print("Charging card")
# Now:
# CardPayment().process()

# outputs:
# Validating payment
# Charging card
# This pattern is extremely useful when the child needs to preserve part of the parent's behavior.

# * Polymorphism
# Polymorphism means that different objects can respond to the same interface in different ways.
# Consider:
#
# payments = [
#     CardPayment(5000),
#     UPIPayment(2000)
# ]
#
# We can write:
#
# for payment in payments:
#     payment.process()
#
# We don't need:
# if isinstance(payment, CardPayment):
#     ...
# elif isinstance(payment, UPIPayment):
#     ...
#
#  Each object knows how to implement:
# process()


# ****Duck typing
#
# Python often takes polymorphism even further.
# The objects don't necessarily need to share a parent class.
#
# Suppose:
# class CardPayment:
#
#     def process(self):
#         print("Card")
#
# class UPIPayment:
#
#     def process(self):
#         print("UPI")
#
# class CashPayment:
#
#     def process(self):
#         print("Cash")
# They don't inherit from a common class.
#
# Yet:
#
# payments = [
#     CardPayment(),
#     UPIPayment(),
#     CashPayment()
# ]
#
# for payment in payments:
#     payment.process()
#
# works.
#
# Why?
#
# Python cares about whether the object provides the required behavior.
# This is often summarized as:
# If it behaves like the required object, it can be used like it.
# This is called duck typing.

# *Multiple inheritance
#
# Python allows:
#
# class A:
#     pass
#
# class B:
#     pass
#
# class C(A, B):
#     pass
#
# C inherits from both A and B.
# This can be useful, but it can also introduce complexity.
#
# For example:
# class Logger:
#     def log(self):
#         print("Logging")
#
# class Serializable:
#     def serialize(self):
#         print("Serializing")
#
# class OrderService(Logger, Serializable):
#     pass
# Now:
# service = OrderService()
# service.log()
# service.serialize()
#
# The class gets behavior from both parents.
#
# 17. The diamond problem
# Multiple inheritance becomes more interesting here:
#
#        A
#       / \
#      B   C
#       \ /
#        D
#
# Suppose both B and C inherit from A, and D inherits from both.
# Which version of a method should Python use?
# *Python solves this using MRO — Method Resolution Order.

