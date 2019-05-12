# got_yr_number.py

phone_number = int(input())

new_number = str(phone_number)

first_set = str(new_number[0] + new_number[1] + new_number[2])
second_set = str(new_number[3] + new_number[4] + new_number[5])
third_set = str(new_number[6] + new_number[7] + new_number[8] + new_number[9])

print(first_set + '-' + second_set + '-' + third_set)