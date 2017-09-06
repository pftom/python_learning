filename = 'trash2.txt'

with open(filename, 'a') as file_object:
    file_object.write("I love you.\n")
    file_object.write("I love hiking.\n")
    file_object.write("I love running.\n")
    file_object.write("I love swimming.")