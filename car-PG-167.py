class Car():

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):

        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
            """Add the given amount to the odometer reading."""
            self.odometer_reading += miles

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")



my_new_car = Car('Audi', 'a4', 2016)

print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(2500)
my_new_car.increment_odometer(100)
my_new_car.read_odometer()



class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())