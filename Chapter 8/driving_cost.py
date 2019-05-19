def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    answer = driven_miles / miles_per_gallon * dollars_per_gallon
    return answer

if __name__ == '__main__':
    u_mpg = float(input())
    u_cpg = float(input())
    a_10 = driving_cost(10, u_mpg, u_cpg)
    a_50 = driving_cost(50, u_mpg, u_cpg)
    a_400 = driving_cost(400, u_mpg, u_cpg)

    print('%.2f' % a_10)
    print('%.2f' % a_50)
    print('%.2f' % a_400)