# Class Variables
class Car:
    total_car = 0  # initially 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1  # to make it update

    def get_brand(self):
        return self.__brand + "!"

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)

    def full_name(self):
        return f"{self.__brand} {self.model} {self.battery_size}"

    def fuel_type(self):
        return "Electric Charge"


my_car = ElectricCar("Tesla", "Rawr", "10m")
print(my_car.model)
print(my_car.fuel_type())

safari = Car("Tata", "Safari")
safariThree = Car("Tata", "Nexon")
print(safari.fuel_type())

# test = Car("Test", "test")

print(safari.total_car)  # is ojbect se nhi lete hum
print(Car.total_car)
