"""
What data does this object contain?
Conceptually:
Object
├── Identity
├── Type
└── Value
Example:
age = 21
The object has:
identity → unique identity
type     → int
value    → 21
You can inspect two of these directly:
type(age)
id(age)



Reassignment doesn't modify the old object
Consider:
x = 100
y = x
x = 200
Now:
x ─────→ 200
y ─────→ 100
x = 200 did not change the object 100.
It changed what the name x refers to.
This distinction becomes very important with mutable objects.



Python is dynamically typed and strongly typed.
For example:
age = 21
result = age + " years"
This doesn't silently convert " years" into something compatible with int.
You'll get a TypeError.
Python doesn't generally perform arbitrary implicit conversions just to make incompatible operations work.



Built-in types

Python provides many built-in data types.
For our current stage, know these major categories:
Numeric
int
float
complex

Boolean
bool

Text
str

Null-like
NoneType



Python integers can become very large; they aren't limited to a typical fixed 32-bit/64-bit range like many languages.
huge_number = 123456789012345678901234567890


complex
Python supports complex numbers:
z = 3 + 4j
You can access:
print(z.real)
print(z.imag)
Output:
3.0
4.0


"""
#Task 1
"""
Imagine an API has received these values:
user_id = "105"
age = "22"
account_balance = "1500.75"
is_verified = "True"

Your job:
Inspect the types.
Convert the numeric values into appropriate Python types.
Determine an appropriate way to represent the verification state.
Print the final values and their types.
Create a variable called last_login whose value represents "no login recorded yet."
Restrictions

Don't use:
lists
dictionaries
functions
classes
loops
"""
user_id = "105"
age = "22"
account_balance = "1500.75"
is_verified = "True"

#1
print("Type of the user id ",type(user_id))
print("Type of the age ",type(age))
print("Type of the account balance ",type(account_balance))
print("Type of the is_verified ",type(is_verified))

#2
user_id_updated = int(user_id)
age_updated = int(age)
account_balance_updated = float(account_balance)

#3
is_verified_updated = bool(is_verified)

#4
print("Converting user id ",user_id_updated ," and the type ",type(user_id_updated))
print("Converting age ",age_updated," and the type ",type(age_updated))
print("Converting account balance ",account_balance_updated," and the type ",type(account_balance_updated))
print("Is the user verified ",is_verified_updated," and the type ",type(is_verified_updated))

#5
last_login = False

#Task 2
"""
Without running the code initially, predict the result:

a = 500
b = a
c = b

print(a)
print(b)
print(c)

print(a is b)
print(b is c)

"""
a = 500
b = a
c = b

print(a) #500
print(b) #500
print(c) #500

print(a is b) #True
print(b is c) #True

#Task 3
"""
Dynamic Typing
Predict what happens:

data = 100
print(type(data))
data = "100"
print(type(data))
data = 100.0
print(type(data))
data = None
print(type(data))
"""
data = 100
print(type(data)) #int
data = "100"
print(type(data)) #string
data = 100.0
print(type(data)) #float
data = None
print(type(data)) #None