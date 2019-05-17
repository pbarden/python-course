user_score = 0
simon_pattern = 'RRGBRYYBGY'
user_pattern  = 'RRGBBRYBGY'

count = 0

for n in range(len(simon_pattern)):
    if user_pattern[n] == simon_pattern[n]:
        user_score += 1
    else:
        break

print('User score:', user_score)