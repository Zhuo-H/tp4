from dataclasses import dataclass, field
import random
from tkinter.font import names


def dice(max):
    result = random.randint(1, max)
    return result
@dataclass
class Hero:
    name: str
    hp: int = dice(10) + dice(10)
    attaque: int = dice(6)
    defence: int = dice(6)
    force: int = dice(20)
    dexterity: int = dice(20)
    intelligence: int = dice(20)
    charisma: int = dice(20)
    constitution: int = dice(20)
    wisdom: int = dice(20)

    def faire_attaque(self):
        damage = self.attaque + dice(6)
        print(damage)
    def take_damage(self, t_damage):
        self.hp -= t_damage
        print(self.hp)
    def alive(self):
        if self.hp <= 0:
            print("you are dead")
            return False


h1 = Hero("Gerald")
h1.faire_attaque()
h1.take_damage(10)
h1.alive()


