#from dataclasses import dataclass
import random



def dice(max):
    result = random.randint(1, max)
    return result

def picker():
    rolls = [dice(6) for _ in range(4)]
    rolls_sorted = sorted(rolls, reverse = True)
    return sum(rolls_sorted[:3])


class NPC:
    def __init__(self, name):
        self.armor = dice(12)
        self.hp = dice(20)
        self.force = picker()
        self.dexterity = picker()
        self.constitution = picker()
        self.intelligence = picker()
        self.charisma = picker()
        self.sagesse = picker()
        self.name = name
    def stats(self):
        print(f"stats of: {self.name}")
        print(f"Name: {self.name}")
        print(f"Armor: {self.armor}, HP: {self.hp}, Force: {self.force}, Dexterity: {self.dexterity}")
        print(f"Constitution: {self.constitution}, Intelligence: {self.intelligence}, Charisma: {self.charisma}")
        print(f"Sagesse: {self.sagesse}\n")

    def attaque(self, target):
        self.damage = dice(6)
        target.hp -= self.damage
        print(f"{self.name} hit {target.name} for {self.damage}!\n")


    def talk(self, message):
        print(f"{self.name}: {message}\n")

class kobold(NPC):
    pass

class hero(NPC):
    pass

jeff = hero("Jeff")
jeff.stats()
kobold = kobold("Kobold the 1.294037 * 10^8 th")
kobold.stats()
jeff.attaque(kobold)
kobold.talk("ow")
kobold.stats()

