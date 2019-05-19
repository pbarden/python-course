def steps_to_miles(user_steps):
    num_miles = user_steps / 2000.00
    return num_miles

if __name__ == '__main__':
    u_steps = float(input())
    answer = steps_to_miles(u_steps)
    print('%.2f' % answer)