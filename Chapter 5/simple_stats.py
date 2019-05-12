# simple_stats.py

num1 = float(input())
num2 = float(input())
num3 = float(input())

int_avg = int(num1 + num2 + num3) / 3
int_prod = int(num1 * num2 * num3)

float_avg = float(num1 + num2 + num3) / 3
float_prod = float(num1 * num2 * num3)

print('%d %d' % (int_avg, int_prod))
print('%.2f %.2f' % (float_avg, float_prod))