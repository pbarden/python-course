full_name = input()

f_name = full_name.split(' ')

if len(f_name) == 3:
    first_name = f_name[0]
    middle_init = f_name[1][0]
    last_name = f_name[2]
    
    print('{2}, {0} {1}.'.format(first_name, middle_init, last_name))
else:
    first_name = f_name[0]
    last_name = f_name[1]
    
    print('{1}, {0}'.format(first_name, last_name))