def write_name(name):
    filename = 'guest.txt'

    with open(filename, 'a') as file_object:
        file_object.write(name + "\n")
        print("Welcome to Powerformer " + name)