# pass_maker.py

# FIXED 
# Output all the values on a single line
favorite_color = input('Enter favorite color:\n')
pets_name = input('Enter pet\'s name:\n')
a_number = int(input('Enter a number:\n'))

print('You entered:', favorite_color, pets_name, a_number)

# FIXED
password1 = favorite_color
print('\nFirst password: %s_%s' % (favorite_color, pets_name))
print('Second password: %d%s%d' % (a_number, favorite_color, a_number))

# FIXED
pass1 = favorite_color + '_' + pets_name
pass2 = str(a_number) + favorite_color + str(a_number)

p_len1 = len(pass1)
p_len2 = len(pass2)

print('\nNumber of characters in %s: %d' % (pass1, p_len1))
print('Number of characters in %s: %d' % (pass2, p_len2))
