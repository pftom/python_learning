banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

if banned_users:
    print('Is not empty')

not_banned_users = []
if not_banned_users:
    print('Is empty')
else:
    print('empty list is not simple False')


print('-------')
user_list = []