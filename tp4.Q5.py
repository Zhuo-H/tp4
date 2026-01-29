""""""""""

TOUS LES INFOS SONT DANS README.md

"""""""""

import random
from enum import Enum
from dataclasses import dataclass


class Allignement(Enum):
    LAWFUL_GOOD = 0
    NEUTRAL_GOOD = 1
    CHAOTIC_GOOD = 2
    LAWFUL_NEUTRTAL = 3
    TRUE_NEUTRAL = 4
    CHAOTIC_NEUTRAL = 5
    LAWFUL_EVIL = 6
    NEUTRAL_EVIL = 7
    CHAOTIC_EVIL = 8

@dataclass
class Item:
    qte: int
    name: str

class Backpack:

    def __init__(self):
        self.item_list = []

    def add_stuff(self, item_to_add: Item):
        found_item = False
        if len(self.item_list) == 0:
            self.item_list.append(item_to_add)
        else:
            for item in self.item_list:
                if item.name == item_to_add.name:
                    item.qte += item_to_add.qte
                    found_item = True
            if not found_item:
                self.item_list.append(item_to_add)

    def remove_stuff(self, item_to_remove: Item):
        for item in self.item_list:
            if item.name != item_to_remove.name:
                continue

            if item.qte < item_to_remove.qte:
                print("not enough")
                return

            item.qte -= item_to_remove.qte
            self.item_removable = False

            if item.qte ==0:
                self.item_list.remove(item)

            return


    def check_bag(self):
        print(self.item_list)


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
        print(f"Allignement: {self.karma}\n")

    def attaque(self, target):
        attack_value = dice(20)
        damage = dice(10)
        if attack_value == 20:
            target.hp -= damage * 2
            print(f"{self.name} hit {target.name} citically hit for {damage}!\n")
        elif attack_value == 1:
            print(f"{self.name} hit {target.name} but missed!\n")
        else:
            target.hp -= damage
            print(f"{self.name} hit {target.name} for {damage}!\n")

    def talk(self, message):
        print(f"{self.name}: {message}\n")

    def check_alive(self):
        if self.hp <= 0:
            print(f"{self.name} is dead")


class Kobold(NPC):
    def __init__(self, name, karma):
        super().__init__(name, karma)


class Hero(NPC):
    def __init__(self, name, karma):
        super().__init__(name, karma)


jeff = Hero("Jeff", Allignement.LAWFUL_GOOD.name)
jeff.stats()
kobold = Kobold("Kobold", Allignement.CHAOTIC_EVIL.name)
kobold.stats()
jeff.attaque(kobold)
kobold.talk("ow")
kobold.stats()
kobold.check_alive()


bag = Backpack()
bag.add_stuff(Item(5, "gold"))
bag.add_stuff(Item(5, "gold"))
bag.add_stuff(Item(5, "silver"))
bag.add_stuff(Item(5, "bronze"))
bag.remove_stuff(Item(10, "gold"))
bag.remove_stuff(Item(20, "gold"))
bag.check_bag()


