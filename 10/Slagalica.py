import random
class Polje(object):

     def __init__(self, broj = 0):
          self.__broj = broj

     @property
     def vratiBroj(self):
          return self.__broj

     @property
     def jeBroj(self):
          if self.__broj != 0:
               return True
          else:
               return False

     @property
     def jePrazno(self):
          if self.__broj == 0:
               return True
          else:
               return False

     def __str__(self):
          if self.jeBroj == True:
               return '%d' % self.__broj
          if self.jePrazno == True:
               return ' '

     def __repr__(self):
          return 'Polje(%s)' % (self.__broj)

class Ploca():

    def __init__(self, broj_redova, broj_stupaca):
        self.__broj_redova = broj_redova
        self.__broj_stupaca = broj_stupaca

    def vratiVelicinuPloce(self):
        return (self.__broj_redova, self.__broj_stupaca)

    def vratiBrojPolja(self):
        return self.__broj_redova * self.__broj_stupaca

    def postaviPlocu(self, brojevi: list) -> list:
        self.__polja = []
        list_len = 0

        for j in range(self.__broj_stupaca):
            novi_red = []
            for i in range(self.__broj_redova):
                novi_red.append(Polje(brojevi[list_len]))
                list_len += 1

            self.__polja.append(novi_red)


    def __iter__(self):
        polja_lista = []

        for brojac1 in self.__polja:
            for brojac2 in brojac1:
                polja_lista.append(brojac2)

        return iter(polja_lista)

    def __str__(self):
        output = ""
        list = self.__iter__()
        list_len = 0

        for el in list:
            output += str(el) + "\t"
            list_len += 1

            if(list_len == self.__broj_redova):
                list_len = 0
                output += "\n"

        return output

class PrikazIgre(object):

     def izaberiVelicinu(self, velicine: list):
          velicina = {}

          while True:
               print("Izaberi velicinu:")

               for brojac in range(len(velicine)):
                    velicina[str(brojac + 1)] = velicine[brojac]

                    print(brojac + 1, ". velicina ", velicine[brojac][0], "x", velicine[brojac][1], sep="")

               odabranaVelicina = str(input("\nOdaberite jednu od navedenih tezina: "))

               print('>>>', odabranaVelicina)

               if odabranaVelicina in velicina:
                    return odabranaVelicina

     def prikaziPlocu(self, ploca:Ploca):
          print(ploca)

     def unesiPolje(self, broj_polja):
          while True:
               unosPolje = input("Unesite broj polja: ")
               print('>>>', unosPolje)

               try:
                    unosPolje = int(unosPolje)
               except:
                    continue

               if unosPolje > 0 and unosPolje < broj_polja:
                    return unosPolje


print('*** test 1 ***')
pi = PrikazIgre()
print(pi.izaberiVelicinu([(3,3), (3,4), (4,4), (2,2)]))

print('*** test 2 ***')
pl = Ploca(3,3)
pl.postaviPlocu([1,2,3,4,5,6,7,8,0])
pi = PrikazIgre()
pi.prikaziPlocu(pl)

print('*** test 3 ***')
pi = PrikazIgre()
print(pi.unesiPolje(9))
print('****')
print(pi.unesiPolje(3))