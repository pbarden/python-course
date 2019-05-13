import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
   'red': 35,
   'blue': 25,
   'green': 23
}

# Prompt user to input wall's width
# Calculate and output wall area
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = float(wall_height * wall_width)
print('Wall area: %d square feet' % wall_area)
   
# Calculate and output the amount of paint in gallons needed to paint the wall
paint_needed = float(wall_area / 350)
print('Paint needed: %.2f gallons' % paint_needed)

# Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
num_cans = int(math.ceil(paint_needed))
print('Cans needed: %d can(s)' % num_cans)

# FIXME (4): Calculate and output the total cost of paint can needed depending on color
my_color = str(input('\nChoose a color to paint the wall:\n'))
color_cost = paint_colors[my_color] * num_cans
print('Cost of purchasing %s paint: $%d' % (my_color, color_cost))