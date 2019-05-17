total = int(input())
fact = int(1)

counter = 1

while counter <= total:
    if total < 0:
        fact = float('nan')
        counter = total + 1
    elif (total == 0) or (total == 1):
        fact = int(1.0)
        counter = total + 1
    else:
        fact *= counter
        counter += 1

print(fact)