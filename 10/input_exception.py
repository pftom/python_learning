def input_two_num():
    """10-6 func for input exception"""

    try:
        num_one = int(input("Please input the first num: "))
    except ValueError:
        print('num_one is not integer!')
    else:
        try:
            num_two = int(input("Please input the second num: "))
        except ValueError:
            print('num_two is not integer!')
        else:
            print(num_one + num_two)


while True:
    input_two_num()
    flag = input("Press yes/no to continue/end this program: ")
    if flag == 'no':
        break
