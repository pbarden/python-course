triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')
v_string = str()

for n in range(0, triangle_height):
    v_string += (triangle_char + ' ')
    print(v_string)