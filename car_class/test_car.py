import time
from car import Car

print("Starting Car Speed Simulation")

my_car = Car(2020, "Toyota")

print("\n--- Accelerating ---")

for count in range(5):
    my_car.accelerate()
    speed = my_car.get_speed()
    print("The car is now running at", speed, "mph.", "|" * speed)

for count in range(5):
    my_car.brake()
print(my_car.get_speed())

speed = my_car.get_speed()

print("Speed:", speed, "|" * speed)
print("|" * speed)