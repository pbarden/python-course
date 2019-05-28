test_grades = [101, 83, 107, 90]
sum_extra = -999 # Initialize 0 before your loop, useless initialization provided by the assignment instructions

sum_extra = 0 # Correct the default, srsly why would -999 be useful here at all!?
for n in test_grades:
    if n > 100:
        sum_extra += n % 100

print('Sum extra:', sum_extra)