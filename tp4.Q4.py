import random

def dice(max):
    result = random.randint(1, max)
    return result
class Hero:
    def __init__(self, nom):
        self.nom = nom
        self.f_attaque = dice(6)
        self.f_defence = dice(6)
        self.vie = dice(10) + dice(10)

    def faire_attaque(self):
        damage = self.f_attaque() + dice(6)
        print(damage)


h1 = Hero("Gerald")
h1.faire_attaque()


