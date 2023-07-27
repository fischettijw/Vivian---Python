class Dog(): 
    def __init__(self, name, age, breed, characteristic):
        self.name = name
        self.age = age
        self.breed = breed
        self.characteristic = characteristic
        
    def print_breeds(self):
        for breed in self.breed:
            print(breed)
            
    def print_characteristic(self):
        for char in self.characteristic:
            print(char)
            
    def print_dog(self):
        print()
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Breed: {self.breed}")
        print(f"Characteristic: {self.characteristic}")
        print()
            
    def read_file(data_file_name):
        file = open(data_file_name, "r")
        file_data = file.read()
        file.close()
        return file_data
    
    def print_file(print_file_name, heading):
        items = Dog.read_file(print_file_name)
        print()
        print(heading.upper())
        print("=======================")
        print(items)


        