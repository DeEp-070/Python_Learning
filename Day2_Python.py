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
last_login = None

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
print(type(data)) #string(str)
data = 100.0
print(type(data)) #float
data = None
print(type(data)) #NoneType

#Task 4
"""
You're building a small order-calculation component.
Given:

item_price = 1499.50
quantity = 3
shipping_charge = 99
discount = 200

Calculate:
subtotal
amount after discount
final amount including shipping
whether the order qualifies for free shipping

Rules:
If final amount before shipping >= 3000:
    shipping is free
Otherwise:
    shipping = 99

Then print:
Subtotal:
After discount:
Shipping:
Final amount:
Free shipping:
Restrictions

For this task, don't use:
lists
dictionaries
functions
loops
classes
if yet
"""
item_price = 1499.50
quantity = 3
shipping_charge = 99
discount = 200

subtotal = item_price*quantity
amount_after_discount = subtotal - discount
print("Subtotal: ",subtotal)
print("After discount: ",amount_after_discount)

if amount_after_discount>=3000:
    total_amount = amount_after_discount
    print("Shipping: NA")
    print("Total amount: ",total_amount)
    print("Free shipping: Qualified")
else:
    total_amount = amount_after_discount+shipping_charge
    print("Shipping: ",shipping_charge)
    print("Total amount: ", total_amount)
    print("Free shipping: Not Qualified")

#Task 5
"""
Answer this prediction before running it:
x = 10
y = 3

print(x / y)
print(x // y)
print(x % y)
print(x ** y)

Also predict:

print(10 + 5 * 2)
print((10 + 5) * 2)

And finally:

a = 100
b = 100

print(a == b)
print(a is b)
"""
x = 10
y = 3

print(x / y) #3.333333
print(x // y) #3
print(x % y) #1
print(x ** y) #1000

print(10 + 5 * 2) #20
print((10 + 5) * 2) #30

a = 100
b = 100

print(a == b) #True
print(a is b) #True



"""
Strings Are Sequences

A string contains characters in an ordered sequence.
name = "Python"
Positions:
 P  y  t  h  o  n
 0  1  2  3  4  5
So:
name[0]
→ "P"
name[3]
→ "h"
Negative indexing:
name[-1]
→ "n"
name[-2]
→ "o"



Strings Are Immutable
This is very important.
You cannot modify an individual character:
name = "Python"
name[0] = "J"
❌ TypeError
Instead, you create a new string:
name = "Jython"
This connects directly to what we learned about objects, references, and mutability.



Slicing

Syntax:

string[start:stop]

stop is excluded.

name = "Python"

name[0:2]

→ "Py"

name[2:5]

→ "tho"

You can omit boundaries:

name[:3]

→ "Pyt"

name[3:]

→ "hon"

Copy-like full slice:

name[:]

→ "Python"

5. Step

You can specify:

string[start:stop:step]

Example:

name[::2]

takes every second character.

And:

name[::-1]

reverses the string.

This is a common Python idiom.

6. String Operations

Concatenation:

first_name = "Deep"
last_name = "Das"

full_name = first_name + " " + last_name

Repetition:

"Hi " * 3

→

Hi Hi Hi

Membership:

"Py" in "Python"

→ True

7. Useful String Methods

You'll use these constantly:

text.lower()
text.upper()
text.strip()
text.replace()
text.split()
text.startswith()
text.endswith()
text.find()
text.count()

Example:

email = "  USER@EXAMPLE.COM  "

clean_email = email.strip().lower()

Result:

user@example.com

This type of normalization is common when processing user input.

8. split()
skills = "Python,SQL,Git"
skills.split(",")

produces separate pieces.

We'll properly learn the resulting list when we reach collections.

9. f-Strings ⭐

This is the preferred modern way to construct many formatted strings.

name = "Deep"
age = 22

message = f"My name is {name} and I am {age} years old."

Result:

My name is Deep and I am 22 years old.

You can put expressions inside:

price = 100
quantity = 3

message = f"Total: {price * quantity}"

→

Total: 300
10. Formatting Numbers
price = 1499.5

print(f"₹{price:.2f}")

Result:

₹1499.50

.2f means two digits after the decimal point.

This is particularly useful for financial display.
"""

# Task 6
"""
Build a small API user-profile formatter.

Given:
first_name = "  ajay  "
last_name = "DAS"
email = "  Ajay.Das@Example.COM "
country = "india"

Produce:
Name: Ajay DAS
Email: ajay.das@example.com
Country: India

Requirements:

remove unnecessary surrounding spaces
normalize the email to lowercase
capitalize the country appropriately
construct the final output using f-strings
don't use lists
don't use dictionaries
don't use functions
don't use loops
"""
first_name = "  ajay  "
last_name = "DAS"
email = "  Ajay.Das@Example.COM "
country = "india"

full_name = first_name.strip().capitalize() + ' ' +last_name.capitalize()
sanitized_email = email.strip().lower()
sanitized_country = country.capitalize()
print("Name: ",full_name)
print("Email: ",sanitized_email)
print("Country: "+sanitized_country)

#Task 7
"""
redict before running
text = "Python"
print(text[0])
print(text[-1])
print(text[1:4])
print(text[:3])
print(text[::2])
print(text[::-1])

And:
value = "  Hello World  "
print(value.strip())
print(value.lower())
print(value.upper())
print(value.replace("World", "Python"))
"""
text = "Python"
print(text[0]) #P
print(text[-1]) #n
print(text[1:4]) #yth
print(text[:3]) #Pyt
print(text[::2]) #Pto
print(text[::-1]) #nohtyP

value = "  Hello World  "
print(value.strip()) #Hello World
print(value.lower()) #hello world
print(value.upper()) #HELLO WORLD
print(value.replace("World", "Python")) #  Hello Python
