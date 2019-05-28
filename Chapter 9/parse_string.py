coat_check = False

while coat_check == False:
    my_string = input('Enter input string:\n')
    
    if my_string == 'q':
        coat_check = True
        break

    while ',' not in my_string:
        print('Error: No comma in string.\n')
        my_string = input('Enter input string:\n')

    word_list = my_string.split(',')

    first_word = word_list[0].strip(' ')
    second_word = word_list[1].strip(' ')

    print('First word: %s' % first_word)
    print('Second word: %s\n' % second_word)