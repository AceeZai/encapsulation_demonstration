class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=1, radius=5, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def get_on(self):
        return self.__on

    def display_info(self):
        print("===== FAN PROFILE =====")
        print("Speed:", self.__speed, f"({self.get_speed_name()})")
        print("Radius:", self.__radius)
        print("Color:", self.__color)
        print("On:", self.__on)