import re

def get_num_of_non_WS_characters(usr_str):
    no_white_sp = usr_str.replace(' ', '')
    return len(no_white_sp)

def get_num_of_words(usr_str):
    my_list = list(usr_str.split())
    return len(my_list)

def fix_capilization(usr_str):
    new_str = str()
    new_list = list(re.split(r'(?<=\.) ', usr_str))
    for n in new_list:
        mod_str = n.lstrip()
        new_str += mod_str.capitalize()
        new_str += ' '
    return new_str

def replace_punctuation(usr_str, exclamation_count=0, semicolon_count=0):
    som_str = str()
    for n in usr_str:
        if n == '!':
            som_str += '.'
            exclamation_count += 1
        elif n == ';':
            som_str += ','
            semicolon_count += 1
        else:
            som_str += n
    print('\nexclamation\_count: %d' % exclamation_count)
    print('semicolon\_count: %d' % semicolon_count)
    return som_str

def shorten_space(usr_str):
    return " ".join(usr_str.split())

def print_menu(usr_str):
    menu_op = ' '
    while menu_op != 'q':
        print('\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Fix capitalization\nr - Replace punctuation\ns - Shorten spaces\nq - Quit')
        menu_op = str(input('\nChoose an option:\n'))

        if menu_op == 'c':
            c_var = get_num_of_non_WS_characters(usr_str)
            print('\nNumber of non-whitespace characters: %d' % c_var)
        if menu_op == 'w':
            w_var = get_num_of_words(usr_str)
            print('\nNumber of words: %d' % w_var)
        if menu_op == 'f':
            f_var = fix_capilization(usr_str)
            print('\nEdited text: %s' % f_var)
        if menu_op == 'r':
            r_var = replace_punctuation(usr_str)
            print('Edited text: %s' % r_var)
        if menu_op == 's':
            s_var = shorten_space(usr_str)
            print('\nEdited text: %s' % s_var)
        # return menu_op, usr_str

if __name__ == '__main__':
    my_text = str(input('Enter a sample text:\n'))
    print('\nYou entered: %s' % my_text)
    print_menu(my_text)
