filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
    contents = file_object.read()
    print(contents.lstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace('Python', 'JavaScript'))