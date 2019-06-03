class CarRecord:
    def __init__(self):
        self.year_made = 0
        self.car_vin = ''

    def __str__(self):
        return ('Year: {}, VIN: {}'.format(self.year_made, self.car_vin))

my_car = CarRecord()
my_car.year_made = 2009
my_car.car_vin = 'ABC321'

print(my_car)