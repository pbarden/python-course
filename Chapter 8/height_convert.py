def height_US_to_cm(feet, inches):
    total_inches = feet * 12 + inches
    cm = total_inches * 2.54
    return cm

feet = int(input('Enter feet: '))
inches = int(input('Enter inches: '))

print('Centimeters:', height_US_to_cm(feet, inches))