# import pyjokes
# print(pyjokes.get_joke())


# print("Hello, World!!")
# name = input("What is your name? ")
# age = input("What is your age? ")
# print(f"I am {name} and I am {age} years old.")

# import os as op

# list = op.listdir()
# print(list)

# for i in list:
#     print(i)



# def adding(a,b):
#     return a+b

# print(adding(34,34))

# number = int(input("Enter the number: "))

# print(number/ "z")

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# # print((num1+num2)/2)

# number = int(input("Enter the number: "))
# print(f"The square of the number {number} is {number ** 2}")

# a = int(input("Enter the number 1: "))
# b = int(input("Enter the number 2: "))

# print("a is greater then b:",a>b)

# name = input("Enter your name: ")
# print(f"Goog Morning, {name}")




student = input("Enter the name of the student: ")
grade = input("Enter the class of the student: ")
roll_no = input("Enter the roll number: ")
date = input("Enter the date of the application: ")
school_name = input("Enter the name of the school: ")
shool_address = input("Enter the address of the school: ")
contact_number = input("Enter the contact number: ")
tothe = input("Enter the person whom you are writing it: ")
tothe_gender = input("Enter the gender of the person whom you are writing to: ")
reason = input("Enter the reason for the absence: (ie: due to fever)")
parent_name = input("Enter the name of the parent: ")
email = input("Enter the email address: ")
absentdatefrom1 = input("Enter the starting date of your absence: ")
absentdatefrom2 = input("Enter the ending date of your absence: ")

if tothe_gender == "male":
    tothe_gender = "Sir"
else:
    tothe_gender = "Ma'am"




template = f"""

{student}
Class - {grade}
{roll_no}
{date}

{tothe}
{school_name}
{shool_address}

Subject: Application for Leave of Absence - {student}

Dear {tothe_gender},

I am writing to request a leave of absence for my child, {student}, who is a student in {grade} at your esteemed institution.

The reason for this absence is {reason}. My child will be absent from school on {absentdatefrom1} to {absentdatefrom2}.

Thank you for your understanding and consideration.

Sincerely,

{parent_name}
{contact_number}
{email}
"""

print(template)