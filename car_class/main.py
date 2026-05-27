class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
my_car = Car(2020)
print(my_car.get_speed())