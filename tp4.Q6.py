from dataclasses import dataclass, field
import random



def dice(y):
    result = random.randint(1, y)
    return result

def picker():
    rolls = [dice(6) for _ in range(4)]
    rolls_sorted = sorted(rolls, reverse = True)
    return sum(rolls_sorted[:3])


@dataclass
class Statistique:
    armor: int = field(default_factory = lambda: dice(12))
    hp: int = field(default_factory = lambda: dice(20))
    force: int= field(default_factory = picker)
    dexterity: int = field(default_factory = picker)
    constitution: int = field(default_factory = picker)
    intelligence: int = field(default_factory = picker)
    charisma: int = field(default_factory = picker)
    sagesse: int = field(default_factory = picker)
    name = str = ""
    damage: int = 0

class NPC(Statistique):

    def stats(self):
        print(f"stats of: {self.name}")
        print(f"Name: {self.name}")
        print(f"Armor: {self.armor}, HP: {self.hp}, Force: {self.force}, Dexterity: {self.dexterity}")
        print(f"Constitution: {self.constitution}, Intelligence: {self.intelligence}, Charisma: {self.charisma}")
        print(f"Sagesse: {self.sagesse}\n")

    def attaque(self, target):
        score = dice(20)
        if score == 20:
            self.damage = dice(6) * 2
            #target.hp -= damage
            print(f"{self.name} critically hit {target.name} for {self.damage}!\n")
        elif score == 1:
            print(f"{self.name} missed {target.name}!\n")
        else:
            self.damage = dice(6)
            #target.hp -= damage
            print(f"{self.name} hit {target.name} for {self.damage}!\n")

    def receive_damage(self, ennemy):
        self.hp -= ennemy.damage

    def talk(self, message):
        print(f"{self.name}: {message}\n")

class Kobold(NPC):
    def __init__(self, name):
        super().__init__(name)

class Hero(NPC):
    def __init__(self, name):
        super().__init__(name)

jeff = Hero("Jeff")
jeff.stats()
kobold = Kobold("Kobold")
kobold.stats()
jeff.attaque(kobold)
kobold.receive_damage(jeff)
kobold.talk("ow")
kobold.stats()
