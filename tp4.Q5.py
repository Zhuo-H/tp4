import random
from enum import Enum


class Allignement(Enum):
    LAWFUL_GOOD = 0
    NEUTRAL_GOOD= 1
    CHAOTIC_GOOD = 2
    LAWFUL_NEUTRTAL = 3
    TRUE_NEUTRAL = 4
    CHAOTIC_NEUTRAL = 5
    LAWFUL_EVIL = 6
    NEUTRAL_EVIL = 7
    CHAOTIC_EVIL = 8


def dice(y):
    result = random.randint(1, y)
    return result


def picker():
    rolls = [dice(6) for z in range(4)]
    rolls_sorted = sorted(rolls, reverse = True)
    return sum(rolls_sorted[:3])


class NPC:
    def __init__(self, name, karma):
        self.armor = dice(12)
        self.hp = dice(20)
        self.force = picker()
        self.dexterity = picker()
        self.constitution = picker()
        self.intelligence = picker()
        self.charisma = picker()
        self.sagesse = picker()
        self.name = name
        self.karma = karma

    def stats(self):
        print(f"stats of: {self.name}")
        print(f"Name: {self.name}")
        print(f"Armor: {self.armor}, HP: {self.hp}, Force: {self.force}, Dexterity: {self.dexterity}")
        print(f"Constitution: {self.constitution}, Intelligence: {self.intelligence}, Charisma: {self.charisma}")
        print(f"Sagesse: {self.sagesse}\n")

    def attaque(self, target):
        attack_value = dice(20)
        damage = dice(10)
        if attack_value == 20:
            target.hp -= damage * 2
            print(f"{self.name} hit {target.name} citically for {damage}!\n")
        elif attack_value == 1:
            print(f"{self.name} hit {target.name} but missed!\n")
        else:
            target.hp -= damage
            print(f"{self.name} hit {target.name} for {damage}!\n")

    def talk(self, message):
        print(f"{self.name}: {message}\n")

    def check_alive(self):
        if self.hp > 0:
            pass
        elif self.hp <= 0:
            print(f"{self.name} is dead")


class Kobold(NPC):
    def __init__(self, name, karma):
        super().__init__(name, karma)


class Hero(NPC):
    def __init__(self, name, karma):
        super().__init__(name, karma)


jeff = Hero("Jeff", Allignement.LAWFUL_GOOD)
jeff.stats()
kobold = Kobold("Kobold", Allignement.CHAOTIC_EVIL)
kobold.stats()
jeff.attaque(kobold)
kobold.talk("ow")
kobold.stats()
kobold.check_alive()

