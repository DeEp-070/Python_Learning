# try:
#     # risky operation
# except:
#     # what to do if it fails

# try:
#     num = int(input("Enter a number: "))
#     print(100/num)
# except:   #This works, but bare except is usually a bad practice
#     print("Something went wrong")

#Exception Summary
# Exception
# │
# ├── SystemExit
# ├── KeyboardInterrupt
# └── Exception
#     │
#     ├── ValueError
#     ├── TypeError
#     ├── IndexError
#     ├── KeyError
#     ├── ZeroDivisionError
#     ├── FileNotFoundError
#     └── ...


try:
    num = int(input("Enter a number: "))
    print(100/num)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("cannot divide by zero")
    """except (ValueError, TypeError): #this can also be applied
        print("Invalid input.") """
# except Exception: #much broader exception clause
#     print("All the other exception")

# The else block
# else runs only when the try block succeeds without an exception.

try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid input.")
else:
    print("Valid number:", number)

# The finally block
# finally executes regardless of whether an exception occurred.
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid input.")
finally:
    print("Execution finished.")

"""full example
try:
    number = int(input("Enter number: "))
    result = 100 / number
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Operation complete.")
"""

#catching exception in object
try:
    num = int("abc")
except ValueError as error:
    error.add_note("Invalid value")
    print(error.__notes__)