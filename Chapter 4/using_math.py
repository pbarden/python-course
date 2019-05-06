# using_math.py
import math

x = float(input())
y = float(input())
z = float(input())

your_value1 = math.sqrt(x)
your_value2 = math.fabs(y - z)
your_value3 = math.factorial(math.ceil(z))

print('%0.2f %0.2f %0.2f' % (your_value1, your_value2, your_value3))

