my_bool = True

while my_bool == True:
    my_str = str(input())
    max = len(my_str)

    if (my_str == 'q') or (my_str == 'quit') or (my_str == 'Quit'):
        my_bool = False
        break
    else:
        my_list = list()
        for n in my_str:
            my_list.append(n)
        my_list.reverse()
        for n in range(0, max):
            print(my_list[n], end='')
        print()