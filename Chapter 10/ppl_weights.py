# (1): Prompt for four weights. Add all weights to a list. Output list.
weight_list = []
weight_list.append(float(input('Enter weight 1:\n')))
weight_list.append(float(input('Enter weight 2:\n')))
weight_list.append(float(input('Enter weight 3:\n')))
weight_list.append(float(input('Enter weight 4:\n')))

print('Weights: ', end='')
print(weight_list)

# (2): Output average of weights.
total = float()
for n in weight_list:
    total += float(n)
my_avg = total / len(weight_list)
print('\nAverage weight: {}'.format(my_avg))

# (3): Output max weight from list.
my_max = max(weight_list)
print('Max weight: %.2f' % my_max)

# (4): Prompt the user for a list index and output that weight in pounds and kilograms.
my_in = int(input('\nEnter a list location (1 - 4):\n'))
w_kg = weight_list[my_in - 1] / 2.2
print('Weight in pounds: %.2f' % weight_list[my_in - 1])
print('Weight in kilograms: %.2f' % w_kg)

# (5): Sort the list and output it.
weight_list.sort()
print('\nSorted list:', end=' ')
print(weight_list)