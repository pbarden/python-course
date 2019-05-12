is_leap_year = False

input_year = int(input())

if ((input_year % 100) == 0) and ((input_year % 400) == 0):
    is_leap_year = True
    print('%d is a leap year.' % (input_year))
elif ((input_year % 100) != 0) and ((input_year % 4) == 0):
    is_leap_year = True
    print('%d is a leap year.' % (input_year))
else:
    print('%d is not a leap year.' % (input_year))