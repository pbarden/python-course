import math

def max_magnitude(user_val1, user_val2):
    if abs(int(user_val1)) > abs(int(user_val2)):
        return user_val1
    else:
        return user_val2

if __name__ == '__main__':
    a = input()
    b = input()
    print(max_magnitude(a, b))
