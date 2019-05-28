my_string = input()
libs = my_string.split()

while libs.count('quit') == 0:
    print('Eating {1} {0} a day keeps the doctor away.'.format(libs[0], libs[1]))
    libs.clear()
    my_string = input()
    libs = my_string.split()