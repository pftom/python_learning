from battery import Battery


class Car():
    """try to modify the attr of thid class"""

    def __init__(self, make, model, year):
        """init the description of this car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """get the descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometers(self):
        """"print the car's odometers"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        set the odometers
        forbid return
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """
        let the odometer incrment miles
        """
        self.odometer_reading += miles


my_new_car = Car('audi', 'a8', '2020')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometers()

my_new_car.odometer_reading = 20
my_new_car.read_odometers()

my_new_car.update_odometer(23)
my_new_car.read_odometers()

my_new_car.update_odometer(22)


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类属性"""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
