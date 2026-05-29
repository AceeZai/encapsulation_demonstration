class Pet:
    def __init__(self, name="", animal_type="", age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self):
        return self.__name

    def set_animal_type(self, animal_type):
        return self.__animal_type

    def set_age(self, age):
        return self.__age

print("Pet name:", my_pet.get_name())
print("Animal Type:", my_pet.get_animal_type())
print("Pet Age:", my_pet.get_age())

my_pet = Pet()
age = int(input("Enter pet's age"))