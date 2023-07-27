from Dog import *
import os
os.system("cls")



joker = Dog("Joker", 13, "Boxer", "Family Pet")
charlie = Dog("Charlie",9, "Pug", "Courageous")

characteristics = Dog.read_file("DogCharacteristics.txt")
breeds = Dog.read_file("DogBreeds.txt")

Dog.print_file("DogCharacteristics.txt", "characteristics")
Dog.print_file("DogBreeds.txt", "breeds")

joker.print_dog()
charlie.print_dog()
