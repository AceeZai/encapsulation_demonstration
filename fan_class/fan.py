import tkinter as tk
from PIL import Image, ImageTk
import os
import time
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

    def get_speed_name(self):

        if self.__speed == Fan.SLOW:
            return "SLOW"

        elif self.__speed == Fan.MEDIUM:
            return "MEDIUM"

        elif self.__speed == Fan.FAST:
            return "FAST"

    def display_info(self):
        print("===== FAN PROFILE =====")
        print("Speed:", self.__speed, f"({self.get_speed_name()})")
        print("Radius:", self.__radius)
        print("Color:", self.__color)
        print("On:", self.__on)

    def display_wind_power(self):

        if self.__speed == Fan.SLOW:
            print("Wind: 🌬")

        elif self.__speed == Fan.MEDIUM:
            print("Wind: 🌬🌬")

        elif self.__speed == Fan.FAST:
            print("Wind: 🌬🌬🌬")

    def show_animation(self):

        if not self.__on:
            print("Fan is OFF")
            return

        window = tk.Tk()
        window.title("Fan Animation")

        label = tk.Label(window)
        label.pack()

        base_dir = os.path.dirname(__file__)

        image_files = [
            "fan_1.jpg",
            "fan_2.jpg",
            "fan_3.jpg",
            "fan_4.jpg"
        ]

        images = []

        for file in image_files:
            image_path = os.path.join(base_dir, file)
            image = Image.open(image_path)
            image = image.resize((250, 250))
            images.append(ImageTk.PhotoImage(image))

        if self.__speed == Fan.SLOW:
            delay = 400
        elif self.__speed == Fan.MEDIUM:
            delay = 200
        else:
            delay = 100

        frame_index = 0

        def animate():
            nonlocal frame_index

            label.config(image=images[frame_index])
            label.image = images[frame_index]

            frame_index = (frame_index + 1) % len(images)

            window.after(delay, animate)

        animate()
        window.mainloop()
