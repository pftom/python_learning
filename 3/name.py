# Tom Powerformer
# 2017-08-24
# list
names = [ 'mRc', 'Tom', 'Tao', 'YaoWu' ]
print('Hello, ' + names[0])
print('Hello, ' + names[1])
print('Hello, ' + names[2])
print('Hello, ' + names[3])


# len
print('--------')
print(len(names))

aliens = []
aliens.append('hhh')
aliens.insert(0, 'heheh')
print(aliens)
del aliens[0]
print(aliens)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owner = motorcycles.pop()
print(motorcycles)
print(last_owner)

#
# 分割线
#

print("\n\n\n")
# practice-1 3-4
dinner_list_people = ['mRc', 'yueyue', 'lijiayi']
print(dinner_list_people[0])
print(dinner_list_people[1])
print(dinner_list_people[2])

#
# 分割线
#

print("\n\n\n")
# practice-1 3-5
print("guest " + dinner_list_people[2] + " can't show up our dinner")
dinner_list_people[2] = 'no_people-1'
print("\n\n\n")
print("Hello " + dinner_list_people[0] + ", would you like show up my dinner")
print("Hello " + dinner_list_people[1] + ", would you like show up my dinner")
print("Hello " + dinner_list_people[2] + ", would you like show up my dinner")


#
# 分割线
#

print("\n\n\n")
# practice-1 3-6
print("Wow, I have found a bigger table")
dinner_list_people.insert(3, 'no-people-2')
dinner_list_people.insert(2, 'no-people-3')

dinner_list_people.append('no-people-4')


print("Hello " + dinner_list_people[0] + ", would you like show up my dinner")
print("Hello " + dinner_list_people[1] + ", would you like show up my dinner")
print("Hello " + dinner_list_people[2] + ", would you like show up my dinner")
print("Hello " + dinner_list_people[3] + ", would you like show up my dinner")
print("Hello " + dinner_list_people[4] + ", would you like show up my dinner")
print("Hello " + dinner_list_people[5] + ", would you like show up my dinner")

#
# 分割线
#

print("\n\n\n")
# practice-1 3-6
print("I'm sorry, my new table cannot delivery on time, So I can only invite two person.")
person_1 = dinner_list_people.pop()
print("I'm sorry, " + person_1)

person_2 = dinner_list_people.pop()
print("I'm sorry, " + person_2)

person_3 = dinner_list_people.pop()
print("I'm sorry, " + person_3)

person_4 = dinner_list_people.pop()
print("I'm sorry, " + person_4)

print("Hi," + dinner_list_people[0] + ", you are luckily.")
print("Hi," + dinner_list_people[1] + ", you are luckily.")


del dinner_list_people[0]
del dinner_list_people[0]
print(dinner_list_people)


