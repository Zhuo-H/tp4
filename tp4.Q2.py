
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcul_aire(self):
        print(self.x * self.y)

    def info(self):
        print(f"la longuer est{self.x} et la largeur est {self.y}")


rectangle1 = Rectangle(20, 4)
rectangle2 = Rectangle(10, 7)

rectangle1.calcul_aire()
rectangle2.calcul_aire()

rectangle1.info()
rectangle2.info()

