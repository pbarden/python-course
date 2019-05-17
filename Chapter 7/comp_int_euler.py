from math import pow
from math import e

a = float(input('Principal:\n'))
b = float(input('Interest rate:\n'))
d = float(input('Time in years:\n'))

n = 1
while n < d:
    my_flt = float(a * pow(e, b * n))
    print('Savings with interest after year %d: $%.2f' % (n, my_flt))
    n += 1

compInt = float(a * pow(e, b * d))
print('Total after year %d: $%.2f' % (d, compInt))