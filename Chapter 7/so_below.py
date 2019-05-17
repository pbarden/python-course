my_list = list()

my_list_len = int(input())

for n in range (0, my_list_len):
    my_list.append(int(input()))

user_val = int(input())

for n in my_list:
    if n <= user_val:
        print(n)