# Some functions are not available during this exercise

user_input = input()

new_list = user_input.split()

my_list = new_list.copy()

for n in my_list:
    if int(n) < 0:
        my_list.remove(n)

my_list.sort(key=int)

pr_string = ''

for n in my_list:
    print(n, end=' ')

[print(n, end=' ') for n in my_list]

pr_string += my_list

print(pr_string)