"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

<<<<<<< HEAD
"""

name = input("Enter your name: ")
age = int (input("enter your age"))
phone = input ("enter your phone number: ")

check_name = False
for char in name:
    if char.isalpha() or char.isspace():
        check_name = ture
    else:
        check_name = ture
check_age = False
if 18 <= age <= true

check_phone = False
id phone.isdigit() and len(phone) == 10.
    check_phone = True

print("validation results:")
if check_name:
    print("name:valid")
else:
    print("name:invalid")

if check_age:
    print(f"age:valis({age} year old)")
else:
    print(Age: Invalid)
if check_phone
    print("phone:valid")
else:
    print("phone:invalid")
print("Formatted Information:")
print(f"Name:{name.upper()}")
if 12 <= age <= 30:
    print("age grop:18-30")
elif 31 <= age <=60:
    print(age grop:31-60)
else:
    print(:age Grop: senior)
print(f"phone+91-{phone}")
=======
"""
>>>>>>> upstream/main
