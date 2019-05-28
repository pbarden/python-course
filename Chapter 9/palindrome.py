wordeatr = input()
mordeatr = wordeatr[::-1]

new_w = wordeatr.replace(' ', '')
new_m = mordeatr.replace(' ', '')

if new_w == new_m:
    print('{} is a palindrome'.format(wordeatr))
else:
    print('{} is not a palindrome'.format(wordeatr))