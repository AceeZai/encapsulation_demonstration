from fan import Fan

fan1 = Fan(Fan.FAST, 10, "yellow", True)
fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

print("Fan 1:", fan1.get_speed(), fan1.get_radius(), fan1.get_color(), fan1.get_on())
print("Fan 2:", fan2.get_speed(), fan2.get_radius(), fan2.get_color(), fan2.get_on())

fan1.display_info()
fan1.display_wind_power()
fan2.display_info()
fan2.display_wind_power()