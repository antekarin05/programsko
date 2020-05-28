class Kruznica(object):

     def __init__(self, r):
          self.r = r

     def __str__(self):
          return "Kruznica radijusa %.2f" % (self.r)

class Kvadrat(object):

     def __init__(self, a):
          self.a = a

     def __str__(self):
          return "Kvadrat stranice %.2f" % (self.a)

if __name__ == "__main__":
     print('*** Test Likovi ***')
     kruznica = Kruznica(3)
     kvadrat = Kvadrat(4.5)
     print(kruznica)
     print(kvadrat)
