print("Starting Fan Class Project")

class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=1, radius=5, color="blue", on=False):
        self.speed = fan.SLOW
        self.on = False
        self.radius = 5
        self.color = "blue"

fan = Fan()

print(fan.speed)
print(fan.radius)
print(fan.color)
print(fan.on)
