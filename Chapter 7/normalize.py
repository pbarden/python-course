my_list = list()

max_m = int(input())

for n in range (0, max_m):
    my_list.append(int(input()))

min_num = my_list[0]

for n in my_list:
    if n < min_num:
        min_num = n

for n in my_list:
    t_num = n - min_num
    print(t_num)