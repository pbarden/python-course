# Write a program that takes in an integer in the range 20-98 as input. The output is a countdown starting from the integer, and stopping when both output digits are identical.

max_num = int(input())

if (20 <= max_num <= 98):
    if max_num >= 88: 
        min_num = 87
    elif max_num >= 77:
        min_num = 76
    elif max_num >= 66:
        min_num = 65
    elif max_num >= 55:
        min_num = 54
    elif max_num >= 44:
        min_num = 43
    elif max_num >= 33:
        min_num = 32
    else:
        min_num = 10
    for n in range(max_num, min_num, -1):
        print(n)
else:
    print('Input must be 20-98')