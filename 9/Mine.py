import random

class Kvadrat(object):

     def __init__(self, broj = 0):
          self.__broj = broj
          self.__otkriven = False
          self.__oznaka = False

     def otkrij(self):
          if self.__otkriven == False and self.__oznaka == False:
               self.__otkriven = True

     def oznaci(self):
          if self.__oznaka == False :
               self.__oznaka = True
          else:
               self.__oznaka = False

     @property
     def jeMina(self):
          if self.__broj == -1:
               return True
          else:
               return False

     @property
     def jeBroj(self):
          if self.__broj != 0 and self.__broj !=-1:
               return True
          else:
               return False

     @property
     def jePrazan(self):
          if self.__broj ==0:
               return True
          else:
               return False

     def __str__(self):
          if self.__oznaka == True:
               return "?"
          if self.__otkriven == False:
               return "."
          else:
               if self.jeMina == True:
                    return "x"
               if self.jeBroj == True:
                    return "%d" % self.__broj
               if self.jePrazan == True:
                    return " "

class Polje(object):

    def __init__(self, velicina, broj_mina):
        self.__velicina = velicina
        self.__broj_mina = broj_mina
        self.__kvadrati = [[Kvadrat() for j in range(velicina)] for i in range(velicina)]

        for mine in range(broj_mina):
            random_num = random.randrange(velicina ** 2)
            j = random_num // velicina
            i = random_num % velicina

            self.__kvadrati[j][i] = Kvadrat(-1)

        for j in range(velicina):
            for i in range(velicina):
                if self.__kvadrati[j][i].jeMina:
                    continue

                br_mina = 0

                for brojac in [-1, 0, 1]:
                    red1 = self.provjeriMine(j - 1, i + brojac)
                    red2 = self.provjeriMine(j, i + brojac)
                    red3 = self.provjeriMine(j + 1, i + brojac)

                    if (red1 == -1):
                        br_mina += 1
                    if (red2 == -1):
                        br_mina += 1
                    if (red3 == -1):
                        br_mina += 1

                self.__kvadrati[j][i] = Kvadrat(br_mina)

    def provjeriMine(self, x, y):
        if x >= 0 and y >= 0 and x < self.__velicina and y < self.__velicina:
            if self.__kvadrati[x][y].jeMina:
                return -1
            else:
                return 0

    def __str__(self):
        output = "   1 2 3 4 5\n  -----------"
        for j in range(self.__velicina):
            output += "\n" + str(j + 1) + "| "
            for i in range(self.__velicina):
                output += str(self.__kvadrati[j][i]) + " "
            output +="|"

        output += "\n  ----------"

        return output


print('*** test 1 ***')
print('*** rezultat varira zbog slucajnog izbora mina koristenjem random modula ***')
p = Polje(5,2)
for red in p._Polje__kvadrati:
     for k in red:
          k.otkrij()
          print(k, end = '|')
     print()

print('*** test 2 ***')
print('*** rezultat varira zbog slucajnog izbora mina koristenjem random modula ***')
p = Polje(5,2)
for red in p._Polje__kvadrati:
     for k in red:
          k.otkrij()
print(p)