def miles_to_laps(user_miles):
    laps = float(user_miles) / 0.25
    return laps

if __name__ == '__main__':
    my_num = input()
    lapz = miles_to_laps(my_num)
    print('%.2f' % lapz)