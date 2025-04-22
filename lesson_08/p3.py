# Inheritance
class Car:
    # def __init__(self, elec, cng, petrol):
    #     self.elec = elec
    #     self.cng = cng
    #     self.petrol = petrol
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)  # upr hamne kr diya h

    def full_name(self):
        return f"{self.brand} {self.model} {self.battery_size}"


my_car = ElectricCar("Tesla", "Rawr", "10m")
print(my_car.model)
print(my_car.full_name())
