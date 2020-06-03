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

class PrikazIgre(object):

     def izaberiTezinu(self, tezina: list):
          tezine = {}

          while True:
               print("Izaberi tezinu: ")
               for brojac in range(len(tezina)):
                    tezine[str(brojac + 1)] = tezina[brojac]

                    print(brojac + 1, ". velicina ", tezina[brojac][0], ", broj mina ",
                           tezina[brojac][1], sep = "")

               odabranaTezina = str(input("\n Odaberite jednu od navedenih tezina: "))

               print('>>>', odabranaTezina)

               if odabranaTezina in tezine:
                    return odabranaTezina


     def prikaziPolje(self, polje: Polje):
          print(polje)

     def unesiAkciju(self, velicina):
          while True:
               koordinata = input("Unesite koordinate: ")
               koordinate = ""
               operacija = ""
               print('>>>', koordinata)

               if "?" in koordinata:
                    operacija = "oznaci"
                    koordinate = koordinata.replace("?", "").strip()
               else:
                    operacija = "otkrij"
                    koordinate = koordinata

               if "," in koordinata:
                    koordinate = koordinate.split(",")
               else:
                    koordinate = koordinate.split(" ")

               try:
                    koordinate = [int(koordinate[0]), int(koordinate[1])]
               except:
                    continue

               if (koordinate[0] > 0 and koordinate[0] <= velicina) and (koordinate[1] > 0 and koordinate[1] <= velicina):
                    return (operacija, koordinate[0], koordinate[1])

print('*** test 1 ***')
pi = PrikazIgre()
print(pi.izaberiTezinu([(9,8), (15,14), (20,18), (30,30)]))

print('*** test 2 ***')
p = Polje(5,2)
pi = PrikazIgre()
pi.prikaziPolje(p)

print('*** test 3 ***')
pi = PrikazIgre()
print(pi.unesiAkciju(9))
print(pi.unesiAkciju(3))