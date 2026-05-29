from pet import Pet
import time
import os
import tkinter as tk
from PIL import Image, ImageTk

my_pet = Pet()

name = input("Enter your pet's name: ")
animal_type = input("Enter your pet's type: ")
age = int(input("Enter your pet's age: "))

my_pet.set_name(name)
my_pet.set_animal_type(animal_type)
my_pet.set_age(age)

print("\nSaving pet information...")
time.sleep(1)

print("\n--- Pet Information ---")

print("Pet Name:", my_pet.get_name())
print("Animal Type:", my_pet.get_animal_type())
print("Pet Age:", my_pet.get_age())

print("\nPet Sound:")
my_pet.pet_sound()

base_dir = os.path.dirname(__file__)
animal = animal_type.lower()

if animal == "dog":
    image_file = "dog.jpg"
elif animal == "cat":
    image_file = "cat.jpg"
elif animal == "bird":
    image_file = "bird.jpg"
elif animal == "cow":
    image_file = "cow.jpg"
elif animal == "fish":
    image_file = "fish.jpg"
elif animal == "frog":
    image_file = "frog.jpg"
else:
    image_file = "dog.png"

image_path = os.path.join(base_dir, image_file)

image = Image.open(image_path)
image = image.resize((250, 250))

window = tk.Tk()
window.title("🐾 Your Pet Profile")

photo = ImageTk.PhotoImage(image)

label = tk.Label(window, image=photo)
label.pack()

label.image = photo

window.mainloop()