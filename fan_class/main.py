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

fan1 = Fan(Fan.FAST, 10, "yellow", True)
fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

print(fan1.speed, fan1.radius, fan1.color, fan1.on)

fan = Fan()
print(fan.__speed)

print(fan.radius)
print(fan.color)
print(fan.on)
