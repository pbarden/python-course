user_text = input()
total = int(0)

for ut in user_text:
    if (ut != ' ') and (ut != '.') and (ut != ','):
        total += 1

print(total)