""""""""""

TOUS LES INFOS SONT DANS README.md

"""""""""

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.aire = 0

    def calcul_aire(self):
        self.aire = self.x * self.y

    def info(self):
        print(f"la longuer est {self.x}, la largeur est {self.y} et l'aire est {self.aire}")


rectangle1 = Rectangle(20, 4)
rectangle2 = Rectangle(10, 7)

rectangle1.calcul_aire()
rectangle2.calcul_aire()

rectangle1.info()
rectangle2.info()

