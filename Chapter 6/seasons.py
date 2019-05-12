input_month = input()
input_day = int(input())

calendar = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

if input_month in calendar:
    month_no = calendar.index(input_month) + 1
    if (month_no == 2) and (0 < input_day < 31):
        season = 'winter'
    elif ((month_no == 4) or (month_no == 6) or (month_no == 9) or (month_no == 11)) and (0 < input_day < 31):
        if month_no == 4:
            season = 'spring'
        elif month_no == 6:
            if input_day <= 20:
                season = 'spring'
            else:
                season = 'summer'
        elif month_no == 9:
            if input_day <= 21:
                season = 'invalid'
            elif input_day >= 30:
                season = 'invalid'
            else:
                season = 'invalid'
        else:
            season = 'autumn'
    elif (0 < input_day < 32):
        if month_no == 3:
            if input_day <= 19:
                season = 'winter'
            else:
                season = 'spring'
        elif month_no == 5:
            season = 'spring'
        elif (month_no == 7) or (month_no == 8):
            season = 'summer'
        elif month_no == 10:
            season = 'autumn'
        else:
            if input_day <= 20:
                season = 'autumn'
            else:
                season = 'winter'
    else:
        season = 'invalid'
else:
    season = 'invalid'

print(season)

