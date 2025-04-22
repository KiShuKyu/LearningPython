# Multiple Inheritance

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

# safari = Car("Tata", "Safari")
# print(safari.model)
# safariThree = Car("Tata", "Nexon")


class Battery:
    def battery_info(self):
        return "this is battery"


class Engine:
    def engine_info(self):
        return "This is Engine"


class ElectricCarTwo(Battery, Engine, Car):  # (inheritance from)
    pass


my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
