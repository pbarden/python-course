def get_user_values():
    list_len = int(input())
    my_list = list()
    for n in range(0, list_len):
        my_list.append(int(input()))
        # print(my_list)
    my_max = int(input())
    return my_list, my_max

def output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    for n in user_values:
        if n <= upper_threshold:
            print(n)

if __name__ == '__main__':
    user_values, upper_threshold = get_user_values()
    output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold)
