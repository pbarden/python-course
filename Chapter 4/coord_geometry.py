import math

x1 = 1.0
y1 = 2.0
x2 = 1.0
y2 = 5.0
point_dist = 0.0

rise = y2 - y1
run = x2 - x1
point_dist = math.sqrt(math.pow(run, 2) + math.pow(rise, 2))
print('Points distance:', point_dist)