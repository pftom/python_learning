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
        long_name = str(self.year + ' ' + self.make + ' ' + self.model)
        return long_name
    
    def read_odometers(self):
        """"print the car's odometers"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a8', '2020')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometers()

