import os
from PIL import Image, ImageTk
from pet import Pet
import tkinter as Tk
import time

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

window = Tk()

window.title("Pet Picture")

animal = my_pet.get_animal_type().lower()

if animal == "dog":
    image = Image.open("pet_class/dog.png")

elif animal == "cat":
    image = Image.open("pet_class/cat.png")

elif animal == "bird":
    image = Image.open("pet_class/bird.png")

elif animal == "cow":
    image = Image.open("pet_class/cow.png")

elif animal == "fish":
    image = Image.open("pet_class/fish.png")

elif animal == "frog":
    image = Image.open("pet_class/frog.png")

else:
    image = Image.open("pet_class/dog.png")

image_path = os.path.join(base_dir, image_file)

image = Image.open(image_path)
image = image.resize((200, 200))

window = tk.Tk()
window.title("Pet Picture")

photo = ImageTk.PhotoImage(image)

label = tk.Label(window, image=photo)
label.pack()

window.mainloop()