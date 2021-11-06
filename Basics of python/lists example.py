
my_list = ["Kirill", "Chekmenev", 17, 11, "Institut Montana Zugerberg"]
for value in my_list:
    print(value)

print(my_list[0])  # Kirill
print(my_list[2])  # 17
print(my_list[-1])  # Institut Montana Zugerberg
print(my_list[1:4])  # ['Chekmenev', 17, 11]
print(my_list[:-1])  # ['Kirill', 'Chekmenev', 17, 11]
my_list.append("good boy")
print(my_list)
# ['Kirill', 'Chekmenev', 17, 11, 'Institut Montana Zugerberg', 'good boy']

my_list.pop(1)
print(my_list)
# ['Kirill', 17, 11, 'Institut Montana Zugerberg', 'good boy']

another_list = ["Some other value", 25, "road to the dream"]
new_list = my_list + another_list
print(new_list)
# ['Kirill', 17, 11, 'Institut Montana Zugerberg', 'good boy', 'Some other value', 25, 'road to the dream']
