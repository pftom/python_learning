def greet_user():
    """显示简单的问候语"""
    print("Hello!")

greet_user()

# 8-1
print("------")

def display_message():
    """打印一条消息"""
    print("I have learned py func in this chapter")

display_message()


# 8-1
print("------")

def favorite_book(book_name):
    """打印我最喜欢的书"""
    print("One of my favorite books is " + book_name)

favorite_book("Dad")

# exp
print("------")

def describe_pet(animal_type, pet_name = 'dahuang'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('whillie', 'hhhh')