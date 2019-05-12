total_change = int(input())

if total_change > 0:
    dollars = int(total_change / 100)
    total_change = total_change % 100
    
    if dollars == 1:
        print('%d dollar' % (dollars))
    elif dollars > 0:
        print('%d dollars' % (dollars))
    
    quarters = int(total_change / 25)
    total_change = total_change % 25

    if quarters == 1:
        print('%d quarter' % (quarters))
    elif quarters > 0:
        print('%d quarters' % (quarters))
    
    dimes = int(total_change / 10)
    total_change = total_change % 10
    if dimes == 1:
        print('%d dime' % (dimes))
    elif dimes > 0:
        print('%d dimes' % (dimes))
    
    nickels = int(total_change / 5)
    total_change = total_change % 5
    
    if nickels == 1:
        print('%d nickel' % (nickels))
    elif nickels > 0:
        print('%d nickels' % (nickels))
    
    pennies = total_change
    
    if pennies == 1:
        print('%d penny' % (pennies))
    elif pennies > 0:
        print('%d pennies' % (pennies))
else:
    print('no change')