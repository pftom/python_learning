current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# flag
print("------")


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


# 7-4
print("--------")


prompt = "\nPlease input the burden of this Pizza："
prompt += "\n Input 'quit' to end this burden input："

active = True
while active:
    burden = input(prompt)
    if burden == 'quit':
        active = False
    else:
        print("We will add this " + burden)

# method Two

print("--------")


prompt = "\nPlease input the burden of this Pizza："
prompt += "\n Input 'quit' to end this burden input："

while True:
    burden = input(prompt)
    if burden == 'quit':
        break
    else:
        print("We will add this " + burden)


print("--------")


prompt = "\nPlease input the burden of this Pizza："
prompt += "\n Input 'quit' to end this burden input："

burden = ''
while burden != 'quit':
    burden = input(prompt)
    if burden != 'quit':
        print("We will add this " + burden)


# 7-5
print("--------")
