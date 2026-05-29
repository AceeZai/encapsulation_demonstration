from pet import Pet
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

# -----------------------
# IMAGE SETUP
# -----------------------
base_dir = os.path.dirname(__file__)
image_file = animal_type.lower() + ".jpg"
image_path = os.path.join(base_dir, image_file)

image = Image.open(image_path)
image = image.resize((250, 250))

# -----------------------
# PET SOUND LOGIC
# -----------------------
animal = animal_type.lower()

if animal == "dog":
    sound = "Woof Woof!"
elif animal == "cat":
    sound = "Meow!"
elif animal == "bird":
    sound = "Tweet Tweet!"
elif animal == "cow":
    sound = "Moo Moo!"
elif animal == "fish":
    sound = "Blub Blub!"
elif animal == "frog":
    sound = "Ribbit Ribbit!"
else:
    sound = "Cute pet sound!"

# -----------------------
# TKINTER WINDOW
# -----------------------
window = tk.Tk()
window.title("🐾 Pet Profile App")

photo = ImageTk.PhotoImage(image)

# IMAGE
img_label = tk.Label(window, image=photo)
img_label.pack()

# INFO TEXT
info = f"""
Name: {my_pet.get_name()}
Type: {my_pet.get_animal_type()}
Age: {my_pet.get_age()}
"""

info_label = tk.Label(window, text=info, font=("Arial", 14))
info_label.pack()

# PET SOUND (NEW PART)
sound_label = tk.Label(window, text=f"Sound: {sound}", font=("Arial", 14, "bold"))
sound_label.pack()

# KEEP IMAGE
img_label.image = photo

window.mainloop()

