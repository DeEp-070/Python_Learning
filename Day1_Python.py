#Task 1
"""
Task: Employee onboarding record
Imagine you're writing the first part of an HR system.
Create variables representing an employee:
employee ID
employee name
department
monthly salary
employment status
joining year
Requirements

Your program should:
Store each piece of information in a meaningful variable.
Follow Python naming conventions.
Print each value.
Change the employment status from inactive to active.
Increase the salary to a new value.
Print the updated information.
Define at least one configuration value as an uppercase constant.
"""
employee_id = 101
employee_name = 'Deep'
department = 'Software Development'
monthly_salary = 50000
employee_status = 'Active'
joining_year = '2024-09-07'
RELOCATION = 'na'

print("----Employee Details----")
print('Id of the Employee',employee_id)
print('Name of the Employee',employee_name)
print('Department of the Employee',department)
print('Salary of the Employee',monthly_salary)
print('Status of the Employee',employee_status)
print('Joining Year of the Employee',joining_year)

employee_status='Inactive'
print('\nEmployment status change to ',employee_status)
monthly_salary+=10000
print('Updated monthly salary',monthly_salary)

#Task 2
"""
Which values are configuration/constants?
Which values belong to the current transaction?
What names would another developer immediately understand?
"""
MAX_TRANSACTION_AMOUNT = 60000
TRANSACTION_TIMEOUT = 30
transaction_amount = 2000