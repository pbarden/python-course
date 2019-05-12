# real_estate.py

current_price = int(input())
last_months_price = int(input())

change = current_price - last_months_price
mortgage = (float(current_price) * 0.045) / 12.0

print('This house is $%d. The change is $%d since last month.' % (current_price, change))
print('The estimated monthly mortgage is $%.2f.' % mortgage)