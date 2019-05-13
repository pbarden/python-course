# Output a menu of automotive services and the corresponding cost of each service. 
services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}

print('Davy\'s auto shop services')
for n, x in services.items():
    print('%s -- $%d' % (n, x))

# Prompt the user for two services from the menu.
first_selection = str(input('\nSelect first service:\n'))
second_selection = str(input('Select second service:\n'))

# Output an invoice for the services selected. Output the cost for each service and the total cost.
# Extend the program to allow the user to enter a dash (-), which indicates no service.
print('\nDavy\'s auto shop invoice\n')
prices = list()

if first_selection in services:
    print('Service 1: %s, $%d' % (first_selection, services[first_selection]))
    prices.append(services[first_selection])
else:
    print('Service 1: No service')

if second_selection in services:
    print('Service 2: %s, $%d' % (second_selection, services[second_selection]))
    prices.append(services[second_selection])
else:
    print('Service 2: No service')

gt = 0
for n in prices:
    gt += n

print('\nTotal: $%d' % gt)