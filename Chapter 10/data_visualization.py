def title_prompt():
    user_title = input('Enter a title for the data:\n')
    print('You entered: {}\n'.format(user_title))
    return user_title

def enter_columns():
    col_1 = input('Enter the column 1 header:\n')
    print('You entered: {}\n'.format(col_1))
    col_2 = input('Enter the column 2 header:\n')
    print('You entered: {}\n'.format(col_2))
    return col_1, col_2

def data_prompt():
    i_check = 0
    comma_count = 0
    is_int = False
    while i_check != -1:
        my_data = input('Enter a data point (-1 to stop input):\n')
        for n in my_data:
            if n == -1:
                i_check = -1
            if n == ',':
                comma_count += 1
        if comma_count == 0:
            pass
        if comma_count == 1:
            pass
        
        d_list = my_data.split(',')
        data_string = str(d_list[0])
        data_integer = int(d_list[1])
        print('Data string: {}'.format(data_string))
        print('Data integer: {}'.format(data_integer))
        return data_string, data_integer

novel_title = title_prompt()
columns = enter_columns()
data_points = data_prompt()