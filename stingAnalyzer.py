# length of the string first and last charecter middle character reversed version check it contains "python " in it or not  (case sensitive)

prompt = input("Enter a string: ")

print(f"length of the string is {len(prompt)}")
print(f"The first character of the string is {prompt[0]}")
print(f"The last character of the string is {prompt[-1]}")

print(f"The reversed string is\n{prompt[::-1]}")

if len(prompt) % 2 == 0:
    middle_index = len(prompt) // 2
    print(f"The middle character(s) is/are: {prompt[middle_index - 1:middle_index + 1]}")
elif len(prompt) % 2 != 0: 
    middle_index = len(prompt) // 2
    print(f"The middle character is: {prompt[middle_index]}")
if "python" in prompt:
    print("The string contains 'python'")
else:
    print("The string does not contain 'python'")

