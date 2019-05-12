import math

angle_elev  = 3.8
shadow_len  = 17.5
tree_height = 0.0

tree_height = math.tan(angle_elev) * shadow_len

print('Tree height:', tree_height)