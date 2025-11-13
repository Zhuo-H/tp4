
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.aire = 0

    def calcul_aire(self):
        self.aire = self.x * self.y
        return self.aire

    def info(self):
        print(f"la longuer est {self.x}, la largeur est {self.y} et l'aire est {self.aire}")


rectangle = Rectangle(20, 4)
rectangle.calcul_aire()
rectangle.info()
