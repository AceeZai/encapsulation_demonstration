print("Starting Fan Class Project")

class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self):
        self.speed = SLOW
        self.on = False

fan = Fan()
print(fan)