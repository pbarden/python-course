# Built-in functions max() and sum() are not available during this exercise

user_input = input()

new_list = user_input.split()

my_list = new_list

my_total = 0

for n in my_list:
    my_total += int(n)

my_avg = int(my_total / len(my_list))

my_max = -999
for n in my_list:
    if int(n) > my_max:
        my_max = int(n)

print(my_avg, my_max)