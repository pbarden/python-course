num_guesses = 3
user_guesses = []

counter = 1

while counter <= num_guesses:
    user_in = int(input())
    user_guesses.append(user_in)
    counter += 1

print(user_guesses)