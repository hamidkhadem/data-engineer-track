
class Pokemon:
    name = "this is the default name"
    type = "this is the default type"
    health = "this is the default health"


Pikachu_obj = Pokemon()
Pikachu_obj.name = "Pikachu"
Pikachu_obj.type = "Electric"
Pikachu_obj.health = 70

print(Pikachu_obj.name)
print(Pikachu_obj.type)
print(Pikachu_obj.health)


Charizard_obj = Pokemon()
Charizard_obj.name = "charizard"
Charizard_obj.type = "Fire"
Charizard_obj.health = 700

print(f"charizard name: {Charizard_obj.name}")
print(f"charizard type: {Charizard_obj.type}")
print(f"charizard health: {Charizard_obj.health}")

