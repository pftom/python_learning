city = ['qinghai', 'xizang', 'changbaishan', 'xinjiang', 'qingdao']
print(city[0])
print(city[1])
print(city[2])
print(city[3])
print(city[4])

print("------")

city_sorted = sorted(city)
print(city_sorted[0])
print(city_sorted[1])
print(city_sorted[2])
print(city_sorted[3])
print(city_sorted[4])

print("------")

print(city[0])
print(city[1])
print(city[2])
print(city[3])
print(city[4])

print("------")
city_reverse_sorted = sorted(city, reverse=True)

print(city_reverse_sorted[0])
print(city_reverse_sorted[1])
print(city_reverse_sorted[2])
print(city_reverse_sorted[3])
print(city_reverse_sorted[4])

print("------")
print(city[0])
print(city[1])
print(city[2])
print(city[3])
print(city[4])

print("------")
city.reverse()
print(city[0])
print(city[1])
print(city[2])
print(city[3])
print(city[4])

print("------")
city.reverse()
print(city[0])
print(city[1])
print(city[2])
print(city[3])
print(city[4])


print("------")
city.sort()
print(city[0])
print(city[1])
print(city[2])
print(city[3])
print(city[4])

print("------")
city.sort(reverse=True)
print(city[0])
print(city[1])
print(city[2])
print(city[3])
print(city[4])


print("------")
object_list = ['river', 'mountain', 'boat', 'ship']
object_list.sort()
print(object_list)

object_list.sort(reverse=True)
print(object_list)

sorted_object_list = sorted(object_list)
print(sorted_object_list)

reverse_sorted_object_list = sorted(object_list, reverse=True)
print(reverse_sorted_object_list)

print("The len of this list is " + str(len(object_list)))

object_list.reverse()
print(object_list)


print("------")
print(object_list[1])