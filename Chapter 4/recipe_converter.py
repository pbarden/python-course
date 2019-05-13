lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))

# Finish reading other items into variables, then output the three ingrdients
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_cups = float(input('Enter amount of agave nectar (in cups):\n'))
total_servings = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields %.2f servings' % total_servings)
print('%.2f cup(s) lemon juice' % lemon_juice_cups)
print('%.2f cup(s) water' % water_cups)
print('%.2f cup(s) agave nectar' % agave_cups)

# Prompt user for desired number of servings. Convert and output the ingredients
desired_servings = float(input('\nHow many servings would you like to make?\n'))

ss_water = water_cups / total_servings
ss_agave = agave_cups / total_servings
ss_juice = lemon_juice_cups / total_servings

print('\nLemonade ingredients - yields %.2f servings' % desired_servings)

desired_juice = ss_juice * desired_servings
desired_water = ss_water * desired_servings
desired_agave = ss_agave * desired_servings

print('%.2f cup(s) lemon juice' % desired_juice)
print('%.2f cup(s) water' % desired_water)
print('%.2f cup(s) agave nectar' % desired_agave)

# Convert and output the ingredients from (2) to gallons
gallons_juice = desired_juice / 16.0
gallons_water = desired_water / 16.0
gallons_agave = desired_agave / 16.0

print('\nLemonade ingredients - yields %.2f servings' % desired_servings)

print('%.2f gallon(s) lemon juice' % gallons_juice)
print('%.2f gallon(s) water' % gallons_water)
print('%.2f gallon(s) agave nectar' % gallons_agave)
