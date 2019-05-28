my_letter = input()
my_string = input()
flag_01 = False
final_string = ''

word_list = my_string.split(' ')
letter_list = list()

for n in word_list:
    if my_letter in n:
        print(n)
