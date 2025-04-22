# Property Decorators
# make it read only


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

    @property  # ek property h jisko me hide krna chahata hun usko sabh acxess nhi kr skte aaur krna h toh mere method ke throught acess kre . 1 baar jo bn chuka h usko overwrite na kr skte use of property decorator
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

safari = Car("Tata", "Safari")
# it should not be changed once it is Safari so we 1st make model private
# safari.model = "City" <-
print(safari.model)


safariThree = Car("Tata", "Nexon")

# print(Car.general_desc())
