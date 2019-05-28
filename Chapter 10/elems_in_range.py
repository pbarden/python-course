user_input = input()
new_list = user_input.split()
my_list = new_list

more_input = input()
ran_list = more_input.split()
rangers = ran_list

print(my_list)
print(rangers)

int_list = ''

for n in my_list:
    if (int(n) >= int(rangers[0])) and (int(n) <= int(rangers[1])):
        int_list += n + ' '

print(int_list, end='')