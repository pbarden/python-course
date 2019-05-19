num_rows = 2
num_cols = 3

my_char = input()

for i in range(num_rows):
    print(my_char, end='')

    for j in range(num_cols - 1):
        i *= j
        print(my_char, end='')

    print()