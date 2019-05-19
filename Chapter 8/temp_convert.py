def c_to_f(c_temp):
    f_temp = c_temp * 1.8 + 32.0
    return  f_temp

temp_c = float(input('Enter temperature in Celsius:\n'))
temp_f = c_to_f(temp_c)

print('Fahrenheit:' , temp_f)