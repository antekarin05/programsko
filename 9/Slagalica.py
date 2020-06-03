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


print('*** test 1 ***')
broj_redova, broj_stupaca = 3, 3
pl = Ploca(broj_redova, broj_stupaca)
print(pl.vratiVelicinuPloce(), pl.vratiBrojPolja())
print()
pl.postaviPlocu([0,8,7,6,5,4,3,2,1])
for red in pl._Ploca__polja:
     for p in red:
          print(p, end = '|')
     print()

print('*** test 2 ***')
pl = Ploca(3, 4)
pl.postaviPlocu([1,2,3,4,5,6,7,8,9,10,11,0])
print(pl)
for p in pl:
     print(p, repr(p))