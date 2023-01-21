
class car():
    def __init__(self, brand, model, color) -> None:
        self.brand = brand
        self.model = model
        self.color = color
    

    def repaint(self, new_color):
        self.color = new_color


audi = car("Audi", "2020", "Black")
print(f"Audi's original color is: {audi.color}")

audi.repaint("Green")
print(f"Audi's new color is: {audi.color}")


nissan = car("Nissan", "2019", "Red")
print(f"Nissan's attributes are: {nissan.brand}, {nissan.model}, {nissan.color}")

nissan.repaint("Grey")
print(f"Nissan's attributes are: {nissan.brand}, {nissan.model}, {nissan.color}")
