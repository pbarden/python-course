hourly_temperature = [90, 92, 94, 95]

my_string = str()

for n in hourly_temperature:
    my_string += str(n)
    if n != hourly_temperature[-1]:
        my_string += ' -> '

print(my_string + ' ')
