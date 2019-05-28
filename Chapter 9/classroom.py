def reverse(x):
    return x[::-1]

def palindrome(y):
    rev = reverse(y)
    if y.replace(' ', '') == rev.replace(' ', ''):
        return True
    else:
        return False

s = input()
ans = palindrome(s)

if ans == 1:
    print(s + ' is a palindrome.')
else:
    print(s + ' is not a palindrome.')