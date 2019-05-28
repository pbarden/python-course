my_string = input()
my_char = my_string[0]
my_string = (my_string.replace(my_char, '', 1)).strip()
count = 0

for n in my_string:
    if n == my_char:
        count += 1

print(count)