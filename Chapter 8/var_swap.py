def swap_values(user_val1, user_val2):
    new_str = user_val2 + ' ' + user_val1
    return new_str

if __name__ == '__main__': 
    i1 = input()
    i2 = input()
    print(swap_values(i1, i2))