# calories_burned.py
age = float(input())
weight = float(input())
heart_rate = float(input())
time = float(input())

calories_man = ((age * 0.2017) - (weight * 0.09036) + (heart_rate * 0.6309) - 55.0969) * time / 4.184
calories_woman = ((age * 0.074) - (weight * 0.05741) + (heart_rate * 0.4472) - 20.4022) * time / 4.184

print('Men: %0.2f calories' % calories_man)
print('Women: %0.2f calories' % calories_woman)