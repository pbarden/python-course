def pyramid_volume(base_length, base_width, pyramid_height):
    pyramid_volume = float((base_length * base_width) * pyramid_height * (1/3))
    return pyramid_volume

print('Volume for 4.5, 2.1, 3.0 is:', pyramid_volume(4.5, 2.1, 3.0))