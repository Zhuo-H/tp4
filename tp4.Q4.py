from dataclasses import dataclass
import random



def dice(limit):
    result = random.randint(1, limit)
    return result

@dataclass
class statistics:
    force: int = dice(20)
    dexterity: int = dice(20)
    constitution: int = dice(20)
    intelligence: int = dice(20)
    charisma: int = dice(20)
    sagesse: int = dice(20)


class Hero:
    def __init__(self, name):
        self.hp = dice(10) + dice(10)
        self.atq = dice(6)
        self.df = dice(6)
        self.name = name

    def faire_attaque(self):
        dmg = dice(6) + self.atq
        return dmg

    def recevoir_dommages(self, qte_dommage):
        self.hp -= qte_dommage

    def est_vivant(self):
        if self.hp <= 0:
            return False
        else:
            return True
