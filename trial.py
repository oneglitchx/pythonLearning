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

# l1 = [34,34,45,56,67,23,7]
# reversed_list = reversed(l1)
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
# s = ""
# for i in reversed_list:
#     s = s + str(i)

# print(s)

# for i in s:
#     i = i + " "
#     i.removesuffix(" ")
#     print(i)
# print(i.split())
# i = i.split()

# number = []
# for interger in i:
#     interger = int(interger)
#     number.append(interger)

# print(number)
# ss = "I am the Best and I am stronger , I am smarter I am better I am better "
# print(len(ss))
# print(ss.removesuffix(" "))
# print(len(ss))



# t1 = (34,34,45,546,657)

# t2 = (4,6,6)

# t3 = t1+t2
# print(t3)
# print(t1+t2)

# a , b,c = t2
# print(a)

# dict1 = {
#     "name": "Mayank Kashyap", "age": 17, "hobbie": "programming"
# }

# print(dict1.items())
# print(dict1.keys())
# print(dict1.values())
# print(dict1.get("name"))
# print(dict1["hobbie"])

# eliminated = dict1.pop("name")

# learning about the dictionaries of the python 

# data = {
#     "name":"Mayank Kashyap", "age":17 , "hobbie": "programming"
# }

# print(data.items())
# print(data.values())
# print(data.keys())
# print(data.get("name"))
# print(data.pop("age"))
# print(data)
# print(data.popitem())

# playaer = {"Mayank", "Joney", "bikeis"}
# print(playaer,len(playaer))
# playaer.add("Wokong")
# print(playaer)


# Program for the exercise of the chapter 5

# progyam to store the meaning of the hini to english words and allowing the user to look up the values

# meanings = {"sundar": "beautiful","buddhiman":"intelligent","accha":"good","swarg":"heaven"}


# lookup = input("Enter the Hindi word to know the meaning: ")
# print(f"The English meaning of {lookup.capitalize()} is {meanings.get(lookup).capitalize()}")


# numb = input("Enter the numbers: ").split()
# ourset = set(numb)
# print(type(ourset))
# print(int(numb))
# print(ourset)

# s = set()

# n = int(input("Enter the number 1: "))
# s.add(n)
# n = int(input("Enter the number 2: "))
# s.add(n)
# n = int(input("Enter the number 3: "))
# s.add(n)
# n = int(input("Enter the number 4: "))
# s.add(n)
# n = int(input("Enter the number 5: "))
# s.add(n)
# n = int(input("Enter the number 6: "))
# s.add(n)
# n = int(input("Enter the number 7: "))
# s.add(n)
# n = int(input("Enter the number 8: "))
# s.add(n)

# print(s)


# dit = {}
# name = input("Enter the names of the friends: ")
# lan = input("Enter the name of the fav language: ")
# dit.update({name : lan})
# name = input("Enter the names of the friends: ")
# lan = input("Enter the name of the fav language: ")
# dit.update({name : lan})
# name = input("Enter the names of the friends: ")
# lan = input("Enter the name of the fav language: ")
# dit.update({name : lan})
# name = input("Enter the names of the friends: ")
# lan = input("Enter the name of the fav language: ")
# dit.update({name : lan})

# print(dit)

# 📌
# # A program to take four numbers form the user and comare it which of them from all is the greatest

# # Taking user unputs
# numb1 = int(input("Enter the number 1 : "))
# numb2 = int(input("Enter the number 2 : "))
# numb3 = int(input("Enter the number 3 : "))
# numb4 = int(input("Enter the number 4 : "))

# # Comparing the one numbers to each 
# if numb1 > numb2 and numb1 > numb3 and numb1 > numb4:
#     print(f"{numb1} is the greatest number.")
# elif numb2 > numb1 and numb2 > numb3 and numb2 > numb4:
#     print(f"{numb2} is the greatest number.")
# elif numb3 > numb2 and numb3 > numb3 and numb3 > numb4:
#    print(f"{numb3} is the greatest number.")
# elif numb4 > numb2 and numb4 > numb3 and numb4 > numb4:
#    print(f"{numb4} is the greatest number.")
# else:
#     print("Enter the valid number.")



# 📌
# Taking user input of the marks of the subjects

# taking 33 marks as the passing marks of each subject and overall 40 percentage is the all overall pssing marks

# mathematics = int(input("Enter the marks obtained in the Mathematics out of 100: "))
# science = int(input("Enter the marks obtained in the Science out of 100: "))
# english = int(input("Enter the marks obtained in the English out of 100: "))

# if (mathematics/100*100) >= 33:
#     print(f"You passed in the mathematics examnination and your percentage is {mathematics/100*100}.")
# else:
#     print(f"You failed in the mathematicse examination and your percentage is {mathematics/100*100}.")
# if (science/100*100) >= 33:
#     print(f"You passed in the science examnination and your percentage is {science/100*100}.")
# else:
#     print(f"You failed in the science examination and your percentage is {science/100*100}.")
# if (english/100*100) >= 33:
#     print(f"You passed in the english examnination and your percentage is {english/100*100}.")
# else:
#     print(f"You failed in the english examination and your percentage is {english/100*100}.")

# if (mathematics+science+english)/100*300 >=40:
#     print(f"You have passed overall the examinations and your overall percentage is {(mathematics+science+english)/300*100}.")
# else:
#     print(f"You have failed the overall examinations  and your overall percentage is {(mathematics+science+english)/300*100}.")



# if (mathematics/100*100) >= 33 and (science/100*100) >= 33 and (english/100*100) >= 33:
#     print("Congratulations !!!!!, You have passed all the examinations.")
# else:
#     print("You failed in all the examinations.")


# 📌

# # The programs checks whether the text or prompt are the spam text or not via using specific key words

# # spam_text is the texts which are spam and it is here to test the program
# spam_texts = [
#     "Congratulations! You've won a FREE iPhone. Click here to claim your prize now!",
#     "Act now! Limited time offer to earn money from home. No experience required!",
#     "You have been pre-approved for a credit card. Get instant access to $5000 cash.",
#     "Buy now and double your income in just 7 days. Risk-free opportunity!",
#     "Urgent: Your account has been compromised. Click the link to secure it immediately.",
#     "This is not a scam! You can make $1000 a day with this exclusive deal!"
# ]


# spam_keywords = [
#     "free",
#     "FREE",
#     "win",
#     "winner",
#     "congratulations",
#     "cash",
#     "urgent",
#     "limited time",
#     "click here",
#     "exclusive deal",
#     "buy now",
#     "cheap",
#     "guarantee",
#     "no cost",
#     "risk-free",
#     "special promotion",
#     "act now",
#     "call now",
#     "instant access",
#     "double your income",
#     "earn money",
#     "extra income",
#     "fast cash",
#     "work from home",
#     "pre-approved",
#     "credit card offer"
# ]

# text = input("Enter the text: ")

# # Logic for detecting spam texts
# for i in spam_keywords:
#     if i in text:
#         print("The text is spam.")
#         break
    
# else:
#     print("The text is not spam.")
    


# 📌

# # Program which will take user name as an input and checks whether the length of the user name is less then 10 charecters or not.
# user_name  = input("Enter the user name: ")
# if len(user_name)>10:
#     print("The user name's length is more than 10 charecters.")
# elif len(user_name)==10:
#     print("The user name's length is equal to 10 charecters.")
# else:
#     print("The user name's length is less than 10 charecters.")

# 📌

usernames = [
    "asura",
    "tamanna_08",
    "mastermind101",
    "admin",
    "ghost_user",
    "cyberhawk",
    "alpha_wolf",
    "zen_monk",
    "root_access",
    "quantum_mind",
    "code_wizard",
    "silentstorm",
    "echo_chamber",
    "dark_knight",
    "python_pro",
    "neo_nova",
    "byte_me",
    "login_buddy",
    "terminal_vision",
    "user_zero",
    "h4ck3rman",
    "data_druid",
    "noobmaster69",
    "shadow_slave",
    "sigma_code"
]

name = input("Enter the user name: ")
if name in usernames:
    print("Yes,Your name is in the database.")
else:
    print("No, Your name is not in the database.")