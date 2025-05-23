# Encapsulation ()
class Car:
    # __brand ka mtlb h ki vo aabh private ho chuka h sirf class ke andr acess ho jaega lekin object call krega ttoh acess nhi hoega toh make it acessable
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):  # this Getter
        return self.__brand + "!"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)

    def full_name(self):
        return f"{self.__brand} {self.model} {self.battery_size}"


my_car = ElectricCar("Tesla", "Rawr", "10m")
print(my_car.model)
# print(my_car.full_name())
print(my_car.get_brand())
