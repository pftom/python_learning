alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])


new_points = alien_0['points']
print("You just earned " + str())


alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


alien_0 = {}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'fast'

if alien_0['speed'] == 'fast':
    x_increment = 3
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 1

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print(favorite_languages)
print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() +
    ".")

print('----')
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print('----')
friend_message = {
    'first_name': 'Powerformer',
    'last_name': 'Tom',
    'age': 21,
    'city': 'shanghai',
    }

print("The first name: " + friend_message['first_name'])
print("The last name: " + friend_message['last_name'])
print("The age: " + str(friend_message['age']))
print("The city: " + friend_message['city'])

for key, value in friend_message.items():
    print("\nKey: " + key)
    if key == 'age':
        print("Value: " + str(value))
    else:
        print("Value: " + value)


print("------")
name = 'hhhhhh hasada'


num_list = [1, 2, 3, 5, 4]
num_list.sort()
print(num_list)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'pyton',
    }

for language in set(favorite_languages.values()):
    print(language)
