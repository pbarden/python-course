num_rows = 2
num_cols = 3

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces

for i in range(1, num_rows + 1):
    my_char = 'A'
    for j in range(num_cols):
        print('%d%c' % (i, my_char), end = ' ')
        my_char = chr(ord(my_char) + 1) 

    
print()