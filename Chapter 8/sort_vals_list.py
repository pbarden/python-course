def is_list_even(my_list):
    has_even = False
    has_odd = False
    for n in my_list:
        if n % 2 == 0:
            has_even = True
        else:
            has_odd = True
    if (has_even == True) and (has_odd == False):
        return True
    else:
        return False

def is_list_odd(my_list):
    has_even = False
    has_odd = False
    for n in my_list:
        if n % 2 == 0:
            has_even = True
        else:
            has_odd = True
    if (has_even == False) and (has_odd == True):
        return True
    else:
        return False
        

if __name__ == '__main__':
    u_list = list()
    list_len = int(input())

    for n in range(0, list_len):
        u_list.append(int(input()))
    
    if (is_list_even(u_list) == True) and (is_list_odd(u_list) == False):
        print('all even')
    elif (is_list_even(u_list) == False) and (is_list_odd(u_list) == True):
        print('all odd')
    else:
        print('not even or odd')