first_item_name = str(input('Enter food item name:\n'))

# Finish reading item price and quantity, then output a receipt
grand_total = 0

first_item_price = float(input('Enter item price:\n'))
first_item_qty = int(input('Enter item quantity:\n'))

total_item_cost = float(first_item_price * first_item_qty)

print('\nRECEIPT')
print('%d %s @ $%.2f = $%.2f' % (first_item_qty, first_item_name, first_item_price, total_item_cost))

grand_total += total_item_cost
print('Total cost: $%.2f\n' % grand_total)

# Read in a second food item name, price, and quantity, then output a second receipt
second_item_name = str(input('\nEnter second food item name:\n'))
second_item_price = float(input('Enter item price:\n'))
second_item_qty = int(input('Enter item quantity:\n'))

grand_total += second_item_price * second_item_qty

my_receipt = [(first_item_qty, first_item_name, first_item_price), (second_item_qty, second_item_name, second_item_price)]

print('\nRECEIPT')
for a, b, c in my_receipt:
    print('%d %s @ $%.2f = $%.2f' % (a, b, c, (float(a * c))))

print('Total cost: $%.2f' % grand_total)

# Add a gratuity and total with tip to the second receipt
percent = '15%'
gratuity = grand_total * .15
new_grand_total = grand_total + gratuity
print('\n%s gratuity: $%.2f' % (percent, gratuity))
print('Total with tip: $%.2f' % new_grand_total)