
def number_of_pennies(num_dollars, num_pennies=0):
    total = num_dollars * 100 + num_pennies
    return total

print(number_of_pennies(5, 6)) # Should print 506
print(number_of_pennies(4))    # Should print 400