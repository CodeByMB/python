inventory = ['zwaard', 'schild', 'gezondheidsdrank']

def gebruik_item(item_naam):
    for item in inventory:
        if item == item_naam:
            print(f'Je gebruikt de {item_naam}.')
            inventory.remove(item_naam)
        else:
            print('Je hebt dit item niet.')

item_naam = input("Welk item wil je gebruiken?: ")
gebruik_item(item_naam)
print(inventory)

class Enemy:
    def __init__(self, naam, health):
        self.naam = naam
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
