
# 7-8
sandwich_orders = ['pastrami', 'a', 'b', 'pastrami', 'pastrami', 'c', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwiche = sandwich_orders.pop()
    print("I already make " + finished_sandwiche + ".")
    finished_sandwiches.append(finished_sandwiche)

print("I have done all the sandwiches")
for sandwich in finished_sandwiches:
    print(sandwich)

# 7-9
print("------")

sandwich_orders = ['pastrami', 'a', 'b', 'pastrami', 'pastrami', 'c', 'pastrami']

print("All the pastrami is gone")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

# 7-10

print("------")
user_holiday_place = {}

active = True
while active:
    name = input("\nSo, what's your name ？")
    holiday_place = input("Where do you want to go on a holiday ？")
    message = input("Want to end up this survey ？： yes/no")

    if message == 'yes':
        active = False
    else:
        user_holiday_place[name] = holiday_place

for name, holiday_place in user_holiday_place.items():
    print(name + " want to go to " + holiday_place)