def count_word(filename):
    """10-10 count the word in the file"""

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except OSError:
        print("I'm sorry " + filename + " is not exists.")
    else:
        print(contents.lower().count('the'))
        print("Total count " + str(len(contents)))


count_word('../pcc//chapter_10/moby_dick.txt')