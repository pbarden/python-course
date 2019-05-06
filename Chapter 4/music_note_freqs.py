# music_note_freqs.py
import math

init_key_freq = int(input())

distance = 1

your_value1 = init_key_freq * (2**(1.0 / 12))**0
your_value2 = init_key_freq * (2**(1.0 / 12))**1
your_value3 = init_key_freq * (2**(1.0 / 12))**2
your_value4 = init_key_freq * (2**(1.0 / 12))**3
your_value5 = init_key_freq * (2**(1.0 / 12))**4

print('%0.2f %0.2f %0.2f %0.2f %0.2f' % (your_value1, your_value2, your_value3, your_value4, your_value5))