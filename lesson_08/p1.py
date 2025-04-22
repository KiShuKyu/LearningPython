# Basic Class and Object

# self.brand (class ke andr ka variable )
# brand and model are (parameters ) given by the user jb vo object bana raha tha us class se
class Car:  # the making of form
    def __init__(self, brand, model):  # init (constructor)
        self.brand = brand
        self.model = model


my_car = Car("Toyota", "Corolla")  # the one who will use this form
print(my_car.brand)
