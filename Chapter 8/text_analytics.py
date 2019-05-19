def get_num_of_characters(input_str):
    return len(input_str)

if __name__ == '__main__':
    easy_string = str(input('Enter a sentence or phrase:\n'))
    print('\nYou entered: %s' % easy_string)
    print('\nNumber of characters: %d' % get_num_of_characters(easy_string))
    no_white = easy_string.replace(' ', '')
    print('String with no whitespace: %s' % no_white)