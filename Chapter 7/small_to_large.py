user_num = int(input())
min_num = user_num
max_num = user_num

while user_num > 0:
    next_num = int(input())
    if next_num < 0:
        user_num = 0
        break
    elif next_num < min_num:
        min_num = next_num
    elif next_num > max_num:
        max_num = next_num

print('%d %d' % (min_num, max_num))