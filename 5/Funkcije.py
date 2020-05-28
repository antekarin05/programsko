import Likovi
import math
from math import pi

def opseg(lik):
     if isinstance (lik, Likovi.Kruznica):
          return 2 * lik.r * pi
     elif isinstance(lik, Likovi.Kvadrat):
          return 4 * lik.a

def povrsina(lik):
     if isinstance (lik, Likovi.Kruznica):
          return math.pow(lik.r, 2) * pi
     elif isinstance (lik, Likovi.Kvadrat):
          return lik.a**2

if __name__ == "__main__":
     print('*** Test Funkcije ***')
     print(opseg.__name__)
     print(povrsina.__name__)