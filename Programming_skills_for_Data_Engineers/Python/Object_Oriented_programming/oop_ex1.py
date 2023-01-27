
# Defining the class
class Pokemon:
    # Defining some attributes in the class
    name = "This is the 'Name' arrtibute"
    type = "This is the 'Type' arrtibute"
    health = "This is the 'Heath' arrtibute"


print("\nPikachu Object")
# Creaing an object from class
Pikachu_obj = Pokemon()  # the '()' are essential here to call the class
print(Pikachu_obj.name)
Pikachu_obj.name = "Pikachu"
Pikachu_obj.type = "Electric"
Pikachu_obj.health = 70

print(f"Pikachu Name: {Pikachu_obj.name}, \n\
    Type: {Pikachu_obj.type}, \n\
    Health: {Pikachu_obj.health}")


print("\nCharizard Object")
# Another object from the same class:
Charizard_obj = Pokemon()  # the '()' are essential here to call the class
print(Charizard_obj.name)
Charizard_obj.name = "Charizard"
Charizard_obj.type = "Fire, Flying"
Charizard_obj.health = 650

print(f"Pikachu Name: {Charizard_obj.name}, \n\
    Type: {Charizard_obj.type}, \n\
    Health: {Charizard_obj.health}")