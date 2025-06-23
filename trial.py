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




# student = input("Enter the name of the student: ")
# grade = input("Enter the class of the student: ")
# roll_no = input("Enter the roll number: ")
# date = input("Enter the date of the application: ")
# school_name = input("Enter the name of the school: ")
# shool_address = input("Enter the address of the school: ")
# contact_number = input("Enter the contact number: ")
# tothe = input("Enter the person whom you are writing it: ")
# tothe_gender = input("Enter the gender of the person whom you are writing to: ")
# reason = input("Enter the reason for the absence: (ie: due to fever)")
# parent_name = input("Enter the name of the parent: ")
# email = input("Enter the email address: ")
# absentdatefrom1 = input("Enter the starting date of your absence: ")
# absentdatefrom2 = input("Enter the ending date of your absence: ")

# if tothe_gender == "male":
#     tothe_gender = "Sir"
# else:
#     tothe_gender = "Ma'am"




# template = f"""

# {student}
# Class - {grade}
# {roll_no}
# {date}

# {tothe}
# {school_name}
# {shool_address}

# Subject: Application for Leave of Absence - {student}

# Dear {tothe_gender},

# I am writing to request a leave of absence for my child, {student}, who is a student in {grade} at your esteemed institution.

# The reason for this absence is {reason}. My child will be absent from school on {absentdatefrom1} to {absentdatefrom2}.

# Thank you for your understanding and consideration.

# Sincerely,

# {parent_name}
# {contact_number}
# {email}
# """

# print(template)

# prompt = input("Enter the string: ")

# a = prompt.find("  ")
# print(a)

# mod = prompt.replace("  "," ")
# print(mod)

# unforamtted = "hey, I am the best\nand nobody is build differernt like me.\nI am destined for grateness"
# print(unforamtted)

# list1 = ["Mayank",34,32.234,True]
# print(list1)
# 
# list1[0] = "Kashyap"
# print(list1)
# list1.append(False)
# print(list1)
# 
# 
# list2 = ["asdf", 34,3543,56456,False]
# list1.insert(3,69)
# list1.sort()
# print(list1.index(69))
# list1.index(69)
# list1.pop(2)
# list1.reverse()
# list1.remove("Kashyap")
# list1.clear()
# list1.extend(list2)
# print(list1)
# 
# sub = list1[::3]
# print(sub)
# 
# 

# tup1 = (23,)
# print(type(tup1))
# # tup1[0] = "Mayank"
# tup1 = list(tup1)




# print(tup1)

# fruits = input("Enter the names of your favourite fruits; ")
# list1 = fruits.title().split()
# print(list1)


# deal = input("Enter the whatever things you got in mind: ")
# n = deal.split()
# n = int(n)
# marks = [34,45,65,6,7,234]
# print(n)


# marks = input("Enter the marks of the students :").split()
# print(marks)
# new = []
# for mark in marks:
#     mark = int(mark)
#     print(mark)
#     # new = new.append(mark)

# print(new)



# listw = [0,0,0,00,0,24,234,345]
# # print(listw.count(0))

# new_list = [1,3,4,5]
# sum = new_list[0]+new_list[1]+new_list[2]+new_list[3]
# print(sum)

# marks = input("Enter the marks: ").split()
# print(marks)

# interger = []
# for i in marks:
#     interger.append(int(i))

# print(interger)
# print(f"The summ of the marks of the all stufents {sum(interger)}")
# print(f"The average marks of the student is {(sum(interger))/len(interger)}")

# l1 = [10, 20, 30, 40]
# sum = 0
# for i in l1:
#     sum = i + sum 
#     print(sum) # To check whether the code is working or not
# print(sum) # The final outoput 

# l1 = [10, 20, 30, 40] # The original version of the list
# # suppose the list if not in arranged manner so we will first sort it
# l1.sort()
# print(f"The maximum value from the list is {l1[len(l1)-1]}")

# prompt = input("Enter the numbers only: ").split()
# numeric_prompt = []
# for i in prompt:
#     numeric_prompt.append(int(i))

# sortted_list = sorted(numeric_prompt)
# print(sortted_list)
# print(numeric_prompt)

# print(prompt)

# Program to check that a particular element exists 
# l1 =  [1, 2, 3, 4, 5]  
# prompt = input("Enter the number which you want to find: ")

# if prompt in l1:
#     print("Yes, it exists in the list.")
# else:
#     print("No, the element does not exists.")


# # Reversing the list
# l1 = [34,34,45,56,67,23,7]
# #the reversed list
# l1.reverse()
# print(l1)

l1 = [34,34,45,56,67,23,7]
reversed_list = reversed(l1)
# print(reversed_list)
# print(l1[::-1])

# l2 = []
# for i in reversed_list:
#     print(i)
#     l2.append(i)

# print(l2)

# s = str(reversed_list)
# print(s)
# for i in s:
#     print(s)
s = ""
for i in reversed_list:
    s = s + str(i)

print(s)

for i in s:
    i = i + " "
    i.removesuffix(" ")
    print(i)
print(i.split())
i = i.split()

number = []
for interger in i:
    interger = int(interger)
    number.append(interger)

print(number)
