""""""""""

TOUS LES INFOS SONT DANS README.md

"""""""""

import math
from dataclasses import dataclass

@dataclass
class Circle:
    rayon: int

    def aire(self):
        a_result = math.pi * self.rayon ** 2
        print(f"Le rayon est {round(a_result, 2)}")

    def circonference(self):
        c_result = 2 * math.pi * self.rayon
        print(f"Le circonference est {round(c_result, 2)}")


c1 = Circle(10)
c1.aire()
c1.circonference()
