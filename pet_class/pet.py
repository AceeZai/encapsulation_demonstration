class Pet:

    def __init__(self, name="", animal_type="", age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def pet_sound(self):
        animal_type_lower = self.__animal_type.lower()

        if self.__animal_type == "dog":
            print("Woof Woof!")

        elif self.__animal_type == "cat":
            print("Meow!")

        elif self.__animal_type == "bird":
            print("Tweet Tweet!")

        elif self.__animal_type == "cow":
            print("MOO MOO!")

        elif self.__animal_type == "fish":
            print("Bloop Bloop")

        elif self.__animal_type == "frog":
            print("Kokak? KOKAK!")

        else:
            print("Cute pet sound!")







