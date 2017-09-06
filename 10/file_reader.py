filename = '../pcc/chapter_10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# 亲测，不算年，几乎所有人的生日都在圆周率内= =！
birthdays = []
for j in range(12):
    for i in range(30):
        birthdays.append('0' + str(j*100 + 1 + i))
print(birthdays)

cnt = 0
for birthday in birthdays:
    if birthday in pi_string:
        cnt += 1

print("Total num: " + str(cnt))
