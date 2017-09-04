def get_formatted_name(first_name, last_name):
    """返回整洁的字符串"""
    full_name = first_name + ' ' + last_name
    return full_name


musician_1 = get_formatted_name('jimi', 'hendrix')
print(musician_1)


def get_formatted_full_name(first_name, last_name, middle_name=''):
    """return charity full name"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician_2 = get_formatted_full_name('jimi', 'hendrix')
print(musician_2)

musician_3 = get_formatted_full_name('john', 'hooker', 'lee')
print(musician_3)


while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit)")

    f_name = input("First name:")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_full_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")