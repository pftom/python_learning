squares = []
for num in range(1, 11):
  square = num**2
  squares.append(square)
print(squares)


print('------')

num = 1
num = 'a'
print(num)

print('------')
digits = [1, 2, 3, 4, 5]
print(min(digits))
print(max(digits))
print(sum(digits))

print('------')

squares = [value**2 + 1 for value in range(1, 10)]
print(squares)

# practice
print('------')

for num in range(1, 21):
  print(num)

print('------')
# nums = list(range(1, 1000001))
# for num in nums:
#   print(num)

# print('------')
# print(min(nums))
# print(max(nums))
# print(sum(nums))

print('------')
nums = list(range(1, 20, 2))
for num in nums:
  print(num)

print('------')
nums = list(range(3, 31, 3))
for num in nums:
  print(num)

print('------')
nums = [value**3 for value in range(1, 11)]
for num in nums:
  print(num)

print('------')
nums = []
for num in range(1, 11):
  num_item = num**3
  nums.append(num_item)
for num in nums:
  print(num)

print('------')
players = [1, 2, 3, 4, 5, 6, 7]
print(min(players[0:3]))
print(sum(players[0:3]))

frient_players = players[:]
frient_players.append(4)
print(players)
print('------')
frient_players = players
print(frient_players == players)
frient_players.append(5)
print(frient_players == players)
print(frient_players)
print(players)

# 切片，practice
print('------')
print(players)
print('The first three items in the list are:')
for num in players[:3]:
	print(num)
print('Three items from the middle of the list are:')
for num in players[2:5]:
	print(num)
print('The last three items in the list are:')
for num in players[5:]:
	print(num)


print('------')
pizzas = ['hh', 'hehe', 'hehehah']
friend_pizzas = pizzas[:]
pizzas.append('xixi')
friend_pizzas.append('hhhhhh')
print('My favorite pizzas are:')
for pizza in pizzas:
	print(pizza)
print('My friend’s favorite pizzas are:')
for pizza in friend_pizzas:
	print(pizza)


print('------')
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print('------')
canteens = ('alibaba', 'baidu', 'tencent', 'xiaomi', 'powerformer')
for canteen in canteens:
  print(canteen)
canteens = ('powerformer', 'powerformer', 'tencent', 'xiaomi', 'powerformer')
for canteen in canteens:
	print(canteen)