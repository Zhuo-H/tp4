from dataclasses import dataclass
import random



def dice(max):
    result = random.randint(1, max)
    return result

def picker():
    rolls = [dice(6) for _ in range(4)]
    rolls_sorted = sorted(rolls, reverse = True)
    return sum(rolls_sorted[:3])


class statistics:
    def __init__(self):
        self.armor = dice(12)
        self.hp = dice(20)
        self.force = picker()
        self.dexterity = picker()
        self.constitution = picker()
        self.intelligence = picker()
        self.charisma = picker()
        self.sagesse = picker()

    def stats(self):
        print(f"Armor: {self.armor}, HP: {self.hp}, Force: {self.force}, Dexterity: {self.dexterity}")
        print(f"Constitution: {self.constitution}, Intelligence: {self.intelligence}, Charisma: {self.charisma}")
        print(f"Sagesse: {self.sagesse}")

