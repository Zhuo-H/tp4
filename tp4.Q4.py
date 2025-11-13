from dataclasses import dataclass, field
import random



def dice(max):
    result = random.randint(1, max)
    return result


@dataclass
class NPCStats:
    force: int = dice(20)
    dexterity: int = dice(20)
    intelligence: int = dice(20)
    charisma: int = dice(20)
    constitution: int = dice(20)
    wisdom: int = dice(20)


class Hero:
    def __init__(self, nom):
        self.stats = NPCStats()
        self.name = nom
        # hp: int = dice(10) + dice(10)
        # attaque: int = dice(6)
        # defence: int = dice(6)

    def print_stats(self):
        print(self.name)
        print(self.stats.force)

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


h1 = Hero('test1')
h2 = Hero('test21')

h1.print_stats()
h2.print_stats()

# h1.faire_attaque()
# h1.take_damage(10)
# h1.alive()
#

