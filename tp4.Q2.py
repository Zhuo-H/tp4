
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcul_aire(self):
        print(self.x * self.y)

    def info(self):
        print(f"la longuer est{self.x} et la largeur est {self.y}")


rectangle = Rectangle(10, 4)
rectangle.calcul_aire()
rectangle.info()
