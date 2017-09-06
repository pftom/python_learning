def read_file_and_handle_exception(filename):
    """10-8 for file handle file read exception"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except OSError:
        # 10-9
        pass
        # 10-8
        # message = "I'm sorry to hear that " + filename + " not exists."
        # with open(filename, 'w') as f_obj_two:
        #     f_obj_two.write(message)
        # print(message)
    else:
        print(contents.split())


filenames = ['cats.txt', 'dogs.txt', 'ducks.txt']
for filename in filenames:
    read_file_and_handle_exception(filename)
        