print("Starting Fan Class Project")

class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=1, radius=5, color="blue", on=False):
        self.__speed = speed
        self.radius = radius
        self.color = color
        self.on = on

    def get_speed(self, speed):
        return self.__speed

    def get_radius(self, radius):
        return self.__radius = radius

    def get_color(self, color):
        return self.__color = color

    def get_on(self, on):
        return self.__on = on

fan1 = Fan(Fan.FAST, 10, "yellow", True)
fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

print("Fan 1 Speed:", fan1.get_speed())
print("Fan 2 Speed:", fan2.get_speed())

print(fan.color)
print(fan.on)
