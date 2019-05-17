r_in = input()

ranger = r_in.split(' ')

r1 = int(ranger[0])
r2 = int(ranger[1])

if r1 < r2:
    for n in range(r1, r2, 10):
        print(n, end=' ')
else:
    print('Second integer can\'t be less than the first.')

print()