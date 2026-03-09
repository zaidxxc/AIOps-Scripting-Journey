# Project 2: Build an Employee Profile Generator
# Goal: Practice String Manipulation, Slicing, and F-strings.

first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name

address = '123 Main Street'
address += ', Apartment 4B'
employee_age = 28

employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

years_experience = 5
experience_info = 'Experience: ' + str(years_experience) + ' years'
print(experience_info)

position = 'Data Analyst'
salary = 75000

# Using F-string for clean formatting
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print("-" * 50)
print(employee_card)
print("-" * 50)

# String Slicing Practice
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
year_code = employee_code[4:8]
initials = employee_code[9:11]

print(f"Extracted Department: {department}")
print(f"Extracted Year: {year_code}")
print(f"Extracted Initials: {initials}")