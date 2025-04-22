# Static Method

# print(safari.total_car) (hum dono se value access kr pa rhe the total car ki lekin hume sirf car se total car niklani h toh hum Static method use krte h )
# print(Car.total_car)


class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod  # if using static method dont use self (decorators)
    def general_desc():
        return "Cars are Amazing."


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)

    def full_name(self):
        return f"{self.__brand} {self.model} {self.battery_size}"

    def fuel_type(self):
        return "Electric Charge"


my_car = ElectricCar("Tesla", "Rawr", "10m")

safari = Car("Tata", "Safari")
safariThree = Car("Tata", "Nexon")


# print(safari.general_desc()) # object acess nhi krne chaiyea
print(Car.general_desc())

# print(safari.total_car)
# print(Car.total_car)
