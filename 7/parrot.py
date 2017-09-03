message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# age = int('2.3')
# print(age)

num = input("Please input a int: ")
num = int(num)

if num % 2:
    print("\nThe number " + str(num) + " is odd.")
else:
    print("\nThe number " + str(num) + " is even.")


# 7-1
print("-------")
car = input("What kind of car do you want to len ?")
print("Let me see if I can find you a " + car)

# exmaple
print("-------")
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnert 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)