from math import pow

a = float(input('Principal:\n'))
b = float(input('Interest rate:\n'))
c = float(input('Times compounded yearly:\n'))
d = float(input('Time in years:\n'))

n = 1
while n < d:
    my_flt = float(a * pow(1 + (b / c), c * n))
    print('Savings with interest after year %d: $%.2f' % (n, my_flt))
    n += 1

compInt = float(a * pow(1 + (b / c), c * d))
print('Total after year %d: $%.2f' % (d, compInt))