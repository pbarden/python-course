user_input = input()
new_list = user_input.split()
my_list = new_list

print(my_list)

for n in my_list:
    print(n, my_list.count(n))