total = int(input())

if total > 0:
    fact = int(1)
else:
    fact = str('Undefined.')

counter = 1

while (counter <= total) and (total >= 0):
    if (total == 0) or (total == 1):
        fact = int(1.0)
        break
    else:
        fact *= counter
        counter += 1

print(fact)