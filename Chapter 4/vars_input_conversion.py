# vars_input_conversion.py
user_int = int(input('Enter integer (32 - 126):\n'))
user_float = float(input('Enter float:\n'))
user_char = input('Enter character:\n')
user_str = input('Enter string:\n')

# Finish reading other items into variables, then output the four values on a single line separated by a space
print(user_int, user_float, user_char, user_str)
   
# Output the four values in reverse
print(user_str, user_char, user_float, user_int)

# Convert the integer to a characer, and output that character
print(user_int, 'converted to a character is', chr(user_int))