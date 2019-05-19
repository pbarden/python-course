def is_leap_year(user_year):
    if ((user_year % 100) == 0) and ((user_year % 400) == 0):
        leap_flag = True
    elif ((user_year % 100) != 0) and ((user_year % 4) == 0):
        leap_flag = True
    else:
        leap_flag = False

    return leap_flag

if __name__ == '__main__':
    my_in = int(input())
    ch_flag = is_leap_year(my_in)
    if ch_flag == True:
        print('%d is a leap year.' % my_in)
    else:
        print('%d is not a leap year.' % my_in)