# Class Inheritance and isinstance

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_desc():
        return "Cars are Amazing."

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)

    def full_name(self):
        return f"{self.__brand} {self.__model} {self.battery_size}"

    def fuel_type(self):
        return "Electric Charge"


my_car = ElectricCar("Tesla", "Rawr", "10m")
# isinstance True or False me result dega
print(isinstance(my_car, Car))
print(isinstance(my_car, ElectricCar))

# safari = Car("Tata", "Safari")
# print(safari.model)
# safariThree = Car("Tata", "Nexon")
