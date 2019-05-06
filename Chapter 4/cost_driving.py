# cost_driving.py
miles_gallon = float(input())
dollars_gallon = float(input())

your_value1 = (10 / miles_gallon) * dollars_gallon
your_value2 = (50 / miles_gallon) * dollars_gallon
your_value3 = (400 / miles_gallon) * dollars_gallon

print('%0.2f %0.2f %0.2f' % (your_value1, your_value2, your_value3))
