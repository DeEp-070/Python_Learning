"""
Mini Project: Order Initialization

You're beginning an e-commerce backend.
Create the initial state for one customer order.
Your program should represent:
Customer information
customer ID
customer name
Order information
order ID
product name
quantity
price per item
Order state
payment status
shipping status
Configuration
maximum allowed quantity
standard shipping charge

Then:
Calculate the order's basic total manually using arithmetic.
Store that result in a variable.
Update the payment status.
Update the shipping status.
Print a clean order summary.
Restrictions

Again, no:
lists
dictionaries
functions
loops
classes
if/else
imports

You're intentionally solving a realistic problem using only the concepts we've covered.
Quality requirements

Your code should have:
meaningful variable names
consistent naming
no unnecessary variables
no magic numbers
clear output
sensible constants
"""

#Customer information
customer_id = 101
customer_name="Ajay Das"

#Order information
order_id = 1
product_name= "laptop"
quantity = 1
price_per_item = 60000

#Order state
payment_status = "Cash On Delivery"
shipping_status = 'shipped'

#Configuration
MAXIMUM_ALLOWED_QUANTITY = 10
STANDARD_SHIPPING_CHARGE =99

print('----INVOICE----')
print('Name of the customer ',customer_name)
print("Order id ",order_id)
print("Name of the product ",product_name)
print("Ordered Quantity ",quantity)
print('Total amount ',(quantity*price_per_item)+STANDARD_SHIPPING_CHARGE)
print("Payment status ",payment_status)
print("Shipping Status ",shipping_status)