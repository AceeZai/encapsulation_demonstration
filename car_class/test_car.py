print("Starting Car Speed Simulation")

from car import Car
my_car = Car(2020, Toyota")

print("\n--- Accelerating ---")

for count in range(5):
    my_car.accelerate()
print(my_car.get_speed())