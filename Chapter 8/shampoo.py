def shampoo_instructions(num_cycles):
    my_flag = False
    if num_cycles < 1:
        print('Too few.')
    elif num_cycles > 4:
        print('Too many.')
    else:
        my_flag = True
        for n in range(1, num_cycles + 1):
            print('%d : Lather and rinse.' % n)
    if my_flag ==  True:
        print('Done.')

shampoo_instructions(2)