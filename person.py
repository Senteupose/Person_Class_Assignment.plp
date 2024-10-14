class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello! My name is {self.name}. I am {self.age} years old and I identify as {self.gender}.")

# Create an instance of the Person class
person1 = Person("Alice", 30, "Female")

# Call the introduce method to display the person's information
person1.introduce()
