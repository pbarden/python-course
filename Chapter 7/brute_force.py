# Read in first equation, ax + by = c
a = int(input())
b = int(input())
c = int(input())

# Read in second equation, dx + ey = f
d = int(input())
e = int(input())
f = int(input())

flag = False

for x in range(-10, 10):
    for y in range(-10, 10):
        left = a * x + b * y
        right = d * x + e * y
        if left == c and right == f:
            print(x, y)
            flag = True

if flag == False:
    print('No solution')