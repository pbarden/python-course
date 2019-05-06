# out_with_the_vars.py
user_num = int(input('Enter integer:\n'))
print('You entered:', user_num)
sq_num = user_num * user_num
print(user_num,'squared is', sq_num)
sq_num *= user_num
print('And', user_num, 'cubed is', sq_num, '!!')
print('Enter another integer:')
new_int = int(input())
num_x = user_num + new_int
print(user_num, '+', new_int, 'is', num_x)
num_y = user_num * new_int
print(user_num, '*', new_int, 'is', num_y)