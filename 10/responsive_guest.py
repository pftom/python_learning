from guest import write_name

while True:
    name = input("What's you name, bubby ?\n")
    write_name(name)
    res = input("press yes/no to continue/end this program: ")
    if res == 'no':
        break