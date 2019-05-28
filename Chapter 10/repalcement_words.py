user_input = input()
new_list = user_input.split()
my_list = new_list

other_input = input()
nuevo_list = other_input.split()
mio_list = nuevo_list

for x in my_list[::2]:
    mio_list = [n.replace(x,my_list[(my_list.index(x) + 1)]) for n in mio_list]

strbl = ''
for n in mio_list[:-1]:
    strbl += n + ' '

strbl += mio_list[-1]

print(strbl)