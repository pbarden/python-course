def integer_to_reverse_binary(integer_value):
    as_str = str()
    while integer_value > 0:
        num_val = integer_value % 2
        as_str = str(as_str) + str(num_val)
        integer_value = integer_value // 2
    return as_str

def reverse_string(input_string):
    bk_ward = "".join(reversed(input_string))
    return bk_ward

if __name__ == '__main__':
    user_int = int(input())
    print(reverse_string(integer_to_reverse_binary(user_int)))