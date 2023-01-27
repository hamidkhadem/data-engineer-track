# Defining a class with input paramaters using 'self' 

class Car():
    # function "__init__" is used to initialize the class each time called
    def __init__(self, brand, model, color) -> None:
        self.brnad = brand
        self.model = model
        self.color = color

    # Creating a Method to 'repaint' the car
    def repaint(self, new_color):
        self.color = new_color


# Creating objects from class
audi = Car("Audi", "2020", "Black")
print(f"Audi's currnet color: {audi.color}")

# Calling the method upon Audi car
audi.repaint("Green")
print(f"Audi's new color: {audi.color}")


nissan = Car("Nissan", "2019", "White")
print(f"Nissan's attributes: {nissan.brnad}, {nissan.model}, {nissan.color}")

# Repainting the nissan
nissan.repaint("Grey")
print(f"Nissan's new color: {nissan.color}")