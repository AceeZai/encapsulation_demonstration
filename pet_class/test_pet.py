from tkinter import *
from PIL import Image, ImageTk

from pet import Pet
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

print("=" * 40)
