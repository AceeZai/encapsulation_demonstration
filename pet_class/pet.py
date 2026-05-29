class Pet:
    def __init__(self, name="", animal_type="", age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def get_name(self):
        return self.__name

    def set_animal_type(self, animal_type):
        return self.__animal_type

    def set_age(self, age):
        return self.__age


my_pet = Pet()
age = int("thre")