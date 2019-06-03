some_list = list()
some_list.append(2)
print(some_list[0])
some_list.append(3)
some_list.append(4)
some_list.append(8)

x = int(input())

some_list.append(x)

for i in range(len(some_list)):
    print(some_list[i])

while x > 0:
    some_list.append(x)
    x = int(input())

print(max(some_list))
print(min(some_list))