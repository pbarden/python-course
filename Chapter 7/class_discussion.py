user_val = int(input())

max_val = user_val

while user_val > 0:
    if user_val > max_val:
        print('Before: ', max_val)
        max_val = user_val
        print('After: ', max_val)
    user_val = int(input())

print('Max value:', max_val, end='')