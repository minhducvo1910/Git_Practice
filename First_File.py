#First file and the first commit


#This is my code
print("Hello World!")

#This is a change to the code
class dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} says Woof!")
    def info(self):        
        print(f"{self.name} is a {self.breed}.")
        
name = input("Enter your dog's name: ")
my_dog = dog(name, "Golden Retriever")
my_dog.bark()
my_dog.info()