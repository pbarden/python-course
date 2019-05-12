highway_number = int(input())

if highway_number % 2:
    direction = 'north/south'
else:
    direction = 'east/west'

if (0 < highway_number < 100):
    print('The %d is primary, going %s.' % (highway_number, direction))
elif (100 <= highway_number < 1000):
    serves_hwy = highway_number % 100
    print('The %d is auxiliary, serving the %d, going %s.' % (highway_number, serves_hwy, direction))
else:
    print('%d is not a valid interstate highway number.' % (highway_number))