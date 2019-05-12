x = int(input())
y = int(input())
z = int(input())

if (x < y) and (x < z):
    x_val = x
    x -= x_val
    y -= x_val
    z -= x_val
elif (y < x) and (y < z):
    y_val = y
    x -= y_val
    y -= y_val
    z -= y_val
else:
    z_val = z
    x -= z_val
    y -= z_val
    z -= z_val