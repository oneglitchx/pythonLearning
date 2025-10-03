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

# usernames = [
#     "asura",
#     "tamanna_08",
#     "mastermind101",
#     "admin",
#     "ghost_user",
#     "cyberhawk",
#     "alpha_wolf",
#     "zen_monk",
#     "root_access",
#     "quantum_mind",
#     "code_wizard",
#     "silentstorm",
#     "echo_chamber",
#     "dark_knight",
#     "python_pro",
#     "neo_nova",
#     "byte_me",
#     "login_buddy",
#     "terminal_vision",
#     "user_zero",
#     "h4ck3rman",
#     "data_druid",
#     "noobmaster69",
#     "shadow_slave",
#     "sigma_code"
# ]

# name = input("Enter the user name: ")
# if name in usernames:
#     print("Yes,Your name is in the database.")
# else:
#     print("No, Your name is not in the database.")


# 📌
# write a program to give grades to the students according to the merks scheme

# marks = int(input("Enter the marks of the subject: "))
# if (marks>=90 and marks<=100):
#     print("Your grade in the subject is excellent.")
# elif (marks>=80 and marks<90):
#     print("Your grade in the subject is A.")
# elif (marks>=70 and marks<80):
#     print("Your grade in the subject is B.")
# elif (marks>=60 and marks<70):
#     print("Your grade in the subject is C.")
# elif (marks>=50 and marks<60):
#     print("Your grade in the subject is D.")
# elif (marks<=49):
#     print("Your grade in the subject is F.")

# 📌
# write a program whether a post is talking about Harry or not

# my version of code

# post = input("Enter text of the post: ")
# # print(post)
# if "harry" or "Harry" or 'HARRY' in post:
#     print("The post is talking about Harry.")
# else:
#     print("No, the post is not talking about Harry.")


# code with harry version of code
# post = input("Enter the post text: ")
# if "harry" in post.lower():
#     print("The post is talking about Harry.")
# else:
#     print("The post is not talking about Harry.")

"""
Loops exercises from code with harry
"""

# i = 1
# while(i<51):
#     print(i)
#     i+=1

# l = ["mayank", "kashyap","BAN"]
# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1

# for i in range(101):
#     if i == 69:
#         break
#     print(i)
    
# i = 0 
# while(i<100):
#     if i == 69:
#         i += 1
#         continue
#     print(i)
#     i += 1

# 📌
# program which can print multiplicative table using a for loop 

# number = int(input("Enter the number for the table; "))

# for i in range(1,11):
#     print(f"{number} X {i} = {number*i}")


# 📌
# this program will great the people whose name starts with the letter s
# li = ["Mayank", "Satyam", "Satan"]

# for i in li:
#     if "s" in i.lower():
#         print(f"Good Morning!!, {i}")

# 📌
# program which can print multiplicative table using a while loop 
# number = int(input("Enter the number for the table: "))
# i = 0
# while i<11:
#     print(f"{number} X {i} = {number*i}")
#     i+= 1


# 📌
# this program will print the firt n number of sum using while loop
"""number = int(input("Enter the number till you want the sum of natural numbers: "))
i = 0 
sum = [i for i in range(0,number)]

while i < number:
    ans = sum[i] + sum[i+1]
    print(ans)

"""
# nem = int(input("Enter the number: "))

# i = 0 
# sum = 0
# while i<=nem:
#     sum = sum + i  # sum+= i
#     i += 1
# print(sum)

# 📌
# check weither the number is prime or not

# number = int(input("Enter the number: "))
# for i in range(2,number):
#     if (number%i == 0):
#         print("The number is not prime.")
#         break
#     # else:
#     #     print("Number is a prime")
# else:
#     print("Number is a prime")
    

# 📌
# this program gives the factorial of the number

# number = int(input("Enter the number: "))

# f = 1
# for i in range(1,number+1):
#     if number == 0:
#         break
#     f *= i
# print(f)


# 📌
# printing star pattern
# n = 3
# for i in range(1,n+1):
#     print("*"*i)

# 📌
# printing another star pattern 
"""
   *
  ***
 *****
*******
"""

# n = int(input("Enter the number: "))

# for i in range(1,n+1):
#     print(" " * (n-i) , end="")
#     print("*" * (i*2 -1) )

# print("A"*n)

# 📌
# print the pattern n = 3
'''
* * *
*   *
* * * 

* * * *
*     *
*     *
* * * *
'''
# My version of code without the help of the solution 

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     # if( i == 1 or i == n):
#     #     print("* " * n)
#     if ( i == 1 or i == n):
#         print("* " * n)
#     else:
#         print("*"+" " * (2*i -1) +"*")

# Refined version of code with the help of the solution
# And the above code I misunderstood the problem and pattern making

# n = int(input("Enter the number: "))

# for i in range(1,n+1):
#     if i == 1 or i == n :
#         print("*" * n)
#     else:
#         print("*",end="")
#         print(" " * (n-2), end="")
#         print("*",end="\n")
    
# 📌
# This program will print the table in reverse order
# My way of solvig the problem
# n = int(input("Enter the number: "))
# l = []
# for i in range(1,11):
#     l.append(i)
# # print(l)                          """Insight : Mathematics is the key"""    """Insight : You have to be able to see patterns and translate ideas into mathematical statements"""                                                         
# l.reverse()                         
# # print(l)
# for i in l:
#     print(f"{n} X {i} = {n*i}")

# # Refined way and more efficient way with the help of code with harry
# n = int(input("Enter the number: "))
# for i in range(1,11):
#     print(f"{n} X {11-i} = {n*11-i}")


# practice for functions in python     
# def greet():
#     return "Hello Guys, Chai Pilo"
# g = greet()
# print(g)

"""
            Chapter 8 practice set 
1. Write a program using functions to find greatest of three numbers. 
2. Write a python program using function to convert Celsius to Fahrenheit. 
3. How do you prevent a python print() function to print a new line at the end. 
4. Write a recursive function to calculate the sum of first n natural numbers. 
5. Write a python function to print first n lines of the following pattern: 
*** 
**               - for n = 3 
* 
6. Write a python function which converts inches to cms. 
7. Write a python function to remove a given word from a list ad strip it at the same 
time. 
8. Write a python function to print multiplication table of a given number. 
 
"""
# 📌
# Solution of the problem number 1
# def greater3(a,b, c):
#     if a>b and a>c:
#         return f"{a} is greatest"
#     elif b>a and b>c:
#         return f"{b} is greatest"
#     elif c>a and c>b:
#         return f"{c} is greatest"


# a = greater3(34,654,2342342)

# print(a)


# 📌
# Solution for the question number 2

def ctof(c):
    pass

# 📌
# Solution for the question number 3
# print("Hello, World!", end="")

# 📌
# Solution for the question number 4

# def sum_of_first(n):
#     if n < 0 :
#         return 0
#     return n + sum_of_first(n-1)
#         #  1 0 
# a = sum_of_first(10)
# print(a)

# 📌
# Solution for the question number 5

"""
*** 
**               - for n = 3 
* 
"""

# def patternnn(n):
#     l = []
#     for i in range(1,n+1):
#         l.append(i)
#     l.reverse()
#     for i in l:
#         print(f"*" * i)


# patternnn(5)



# n =3
# l = []
# for i in range(1,n+1):
#     l.append(i)
# l.reverse()
# for i in l:
#     print(f"*" * i)
#     # return f"*" * i


# 📌
# Solution for the question number 6

def inches_to_centimeter(i):
    return i * 2.54


# 📌
# Solution for the question number 7

# def list_word_remover(l,word):
#     for items in l:
#         if (items==word):
#           l.remove(word)


#     for i in new:
#         if i.find(word):
#             i.rstrip(word)
#     return new

# m = ["Mayank", "Kashyap", "yap"]
# print(list_word_remover(m,"yap"))

# li = "Heel is the way to the hell".split()
# # a = list_word_remover(li,"the")
# # print(a)

# list_word_remover(li,"Heel")

# 📌
# Solution for the question number 8
def tables(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

# tables(34)


def list_remove(l,word):
    new = []
    for items in l:
        # new = []
        if not(items == word):
            new.append(items.strip(word))

    # return other
    return new


# m = ["Mayank","kashyap","mayhey","ey"]
# print(list_remove(m , "ey"))




# 📌
# This program is the game of rock, paper and scissor 
# import random

# computer_hand = ["rock","paper","scissor"]
# random.shuffle(computer_hand)
# chand = random.choice(computer_hand)

# human_hand = input("Enter the sign: ").lower()

# # screen output 
# print(f"You choose :{human_hand}\nThe computer choose :{chand}")

# if human_hand == chand:
#     print("Draw")
# else:
#     if human_hand == "rock" and chand == "paper":
#         print("You Lost")
#     elif human_hand == "rock" and chand == "scissor":
#         print("You Won")
#     elif human_hand == "paper" and chand == "rock":
#         print("You Won")
#     elif human_hand == "paper" and chand == "scissor":
#         print("You Lost")
#     elif human_hand == "scissor" and chand == "rock":
#         print("You Lost")
#     elif human_hand == "scissor" and chand == "paper":
#         print("You Won")



# Write
# read
# append
# +
# readline
# readlines
# rb rt 
# with open()

# with open("experimentation.txt","a") as file:
#     apptext = file.write("\nThis is the line on the new line")



# with open("experimentation.txt") as file:
#     conline = file.readline()
#     conline2 = file.readline()
#     print(conline)
#     print(conline2)


# f = open("experimentation.txt","r")
# # text  = f.write(" This is what I wanted")
# contant = f.readlines()
# print(contant)
# f.close()


# 📌
# this program checks is there any word in the specific file
# with open("experimentation.txt","w") as f:
#     f.write("Twinkle Twinkle little star\nHow I wonder what you are\nUp above the world so high like a diamond in the sky.")

# with open("experimentation.txt","r") as f:
#     text = f.read()
#     query = input("Enter the world: ")
#     if query in text:
#         print("Yes")
#     else:
#         print("There is no such word you asked me to search in the file.")


# 📌
# table for the 13 year old 
# def tablekid(n,file_name):
#     with open(file_name, "w") as f:
#         for i in range(1,11): # multiplication of 2
#             t2 = f"{n} X {i} = {n*i}\n"
#             f.write(t2)


# import os
# dirs = "TableOf13yo"
# os.mkdir(dirs)

# for i in range(2,21):
#     tablekid(i,f"table_{i}")
#     os.replace(f"table_{i}",f"TableOf13yo/table_{i}")


# 📌
# Wipeout the contant of a file
# def Wipeout(file):
#     with open(file,"w") as f:
#         f.write("")

# Wipeout("experimentation.txt")

# 📌
# Rename the file to specific name
# import os 
# def reename(fiile,renamed_file="renamed_by_python.txt"):
#     os.replace(fiile,renamed_file)

# reename("experimentation.txt")

# 📌
# Check weither the files are identical and have similar contant
# def checkfilei(file1,file2):
#     f1 = open(file1)
#     f2 = open(file2)
#     contant1 = f1.read()
#     contant2 = f2.read()
#     if file1 == file2:
#         print("The names of the files are similar.")
#     else:
#         print("The names of the file is not similar")
#     if contant1 == contant2:
#         print(f"The contants of {file1} and {file2} are similar.")
#     else:
#         print("The contants of the file are not similar.")
#     f1.close()
#     f2.close()

# checkfilei("c1.txt","c2.txt")


# 📌
# program to make a copy of a file c1.txt 

# 📌
# A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.  

# Reading the file weither therer is the word or not

# with open("c1.txt") as f:
#     contant = f.read()
#     if "Donkey" in contant:
#         print("Donkey is present is the file")
#     else:
#         print("No, Donkey found.")
    
# print(type(contant))
# # Replacing the word Donkey
# with open("c1.txt", "w") as f:
#     f.write(contant.replace("Donkey","#######"))

# 📌
# Repeat the above program for the list of cencored words


# Example paragraph where those words are used
# paragraph = """
# That damn fool thought it was a good idea to start a fire in the woods.
# The idiot nearly burned the whole place down. 
# Sometimes I wonder how such a dumb moron can survive in this world.
# What a jerk — always making stupid choices and dragging others to hell with his crap plans.
# No wonder everyone calls him a loser.
# """
# censored_words = [
#     "damn",
#     "hell",
#     "crap",
#     "stupid",
#     "idiot",
#     "dumb",
#     "jerk",
#     "moron",
#     "fool",
#     "loser"
# ]

# with open("c2.txt") as f:
#     contant = f.read()
#     for word in censored_words:
#         if word in contant:
#             print("This text contains censored words!!!!!!!")
#             break
#         else:
#             print("This text does not contains censored words.")
#             break
# with open("c2.txt","w") as file:
#     for word in censored_words:
#         modified_text = contant.replace(word,"####")
#         contant = modified_text
#     file.write(modified_text)

# 📌 write high score of the hame in the file where ever new high is hit
"""
import random
def game():

    # Generate the random number form the computer
    number = 7

    # Read the file for empty text and replace it with 0
    with open("hi_score.txt") as f :
        highscore = f.read()
    with open("hi_score.txt","w") as f :
        if highscore == "":
            highscore = f.write("0")

    # Giving points
    turn = 0
    while turn < 10:
        ask = int(input("Enter the number: "))
        with open("hi_score.txt") as f:
            score = f.read()

        if ask == number:
            with open("hi_score.txt", "w") as f:
                f.write(str(int(score)+1))
        else:
            with open("hi_score.txt", "w") as f:
                f.write(str(int(score)-1))

        turn+=1
        print(turn)

    with open("hi_score.txt") as f:
        score = f.read()
    print(f"Your high score is {score}")

game()
"""