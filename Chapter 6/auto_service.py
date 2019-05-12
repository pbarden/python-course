desired_service = input('Enter desired auto service:\n')
services_offered = ['Oil change', 'Tire rotation', 'Car wash']
prices = [35, 19, 7]

if desired_service in services_offered:
    print('You entered: %s' % desired_service)
    show_service = desired_service.lower()
    n = services_offered.index(desired_service)
    cost = prices[n]
    print('Cost of %s: $%d' % (show_service, cost))
else:
    print('You entered: %s\nError: Requested service is not recognized' % desired_service)