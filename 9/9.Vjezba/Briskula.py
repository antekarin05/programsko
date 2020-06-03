class Karta(object):
     #kljuc je broj, vrijednosti su (naziv, snaga, bod)
     __karta_info={1: ('as', 11, 10),
                   2: ('duja', 0, 1),
                   3: ('trica', 10, 9),
                   4: ('cetvorka', 0, 2),
                   5: ('petica', 0, 3),
                   6: ('sestica', 0, 4),
                   7: ('sedmica', 0, 5),
                   11: ('fanat', 2, 6),
                   12: ('konj', 3, 7),
                   13: ('kralj', 4, 8)
                   }

     __zogovi = ['kupa', 'spada', 'dinari', 'bastoni']

     @staticmethod
     def brojevi():
          return Karta.__karta_info.keys()

     @staticmethod
     def zogovi():
          return list(Karta.__zogovi)

     def __init__(self, broj, zog, vidljiva=False):
          self.__broj=broj
          self.__zog=zog
          self.__vidljiva=vidljiva

     @property
     def broj(self):
          return self.__broj

     @property
     def zog(self):
          return self.__zog

     @property
     def naziv(self):
          return Karta.__karta_info[self.__broj][0]

     @property
     def bod(self):
          return Karta.__karta_info[self.__broj][1]

     @property
     def snaga(self):
          return Karta.__karta_info[self.__broj][2]

     @property
     def vidljiva(self):
          return self.__vidljiva

     @vidljiva.setter
     def vidljiva(self, value):
          self.__vidljiva=value

     def __repr__(self):
          return self.__class__.__name__+'(%r, %r, %r)' % (self.__broj, self.__zog, self.__vidljiva)

     def __str__(self):
          return self.naziv.title() + ' ' + self.__zog

     @staticmethod
     def jeJaca(zog, kartaPrva, kartaDruga):
          if kartaPrva == zog and kartaDruga.zog == zog:
               return kartaPrva.snaga > kartaDruga.snaga
          elif kartaPrva.zog != zog and kartaDruga.zog == zog:
               return False
          elif kartaPrva.zog == zog and kartaDruga.zog != zog:
               return True
          elif kartaPrva.zog == kartaDruga.zog:
               return kartaPrva.snaga > kartaDruga.snaga
          return True

class Spil(object):

     def __init__(self):
          self.__karte = []
          for zog in Karta.zogovi():
               for broj in Karta.brojevi():
                    self.__karte.append(Karta(broj, zog))

     def __str__(self, red = 5, velicina = 18):
          return '\n'.join(''.join(str(karta).ljust(velicina, ' ')
               for karta in self.__karte[i:i+red])
               for i in range(0, len(self.__karte), red)) + '\n'

     def dajKartu(self, broj_karata = 1):
          daneKarte = []
          while broj_karata>0:
               daneKarte.append(self.__karte.pop())
               broj_karata-=1
          return daneKarte

     def izvadiZog(self):
          kartaZoga = self.__karte.pop()
          self.__karte.insert(0, kartaZoga)
          return kartaZoga

     def promjesaj(self):
          import random
          random.shuffle(self.__karte)

     def imeKarata(self):
          return len(self.__karte)>0

class Igrac(object):

     def __init__(self, ime):
          self.__ime = ime
          self.__karteZaBacanje = []
          self.__karteDobivene = []

     @property
     def ime(self):
          return self.__ime

     @property
     def karteZaBacanje(self):
          return self.__karteZaBacanje

     @karteZaBacanje.setter
     def karteZaBacanje(self, value):
          self.__karteZaBacanje = value

     def baciKartu(self, izbor):
          karta = self.__karteZaBacanje.pop(izbor)
          return karta

     def uzmiKarteZaBacanje(self, karte):
          self.__karteZaBacanje += karte

     def uzmiKarteDobivene(self, karte):
          self.__karteDobivene += karte

     def imaKarataZaBacanje(self):
          return len(self.__karteZaBacanje) > 0

     def bodovi(self):
          return sum(karta.bod for karta in self.__karteDobivene)

     def __str__(self):
          return "Igrac " + self.__ime

class Covjek(Igrac):

     def __init__(self, ime):
          super(Covjek, self).__init__(ime)

class Racunalo(Igrac):

     def __init__(self):
          super(Racunalo, self).__init__("HAL 9000")


'''for zog in Karta.zogovi():
     for broj in Karta.brojevi():
          k=Karta(broj, zog)
          print('%r, %s %d %d' % (k, k, k.bod, k.snaga))

import random

karte = []
for zog in Karta.zogovi():
     for broj in Karta.brojevi():
          karte.append(Karta(broj, zog))

for _ in range(10):
     zog = random.sample(Karta.zogovi(), 1)[0]
     k1, k2 = random.sample(karte, 2)
     poruka = 'je jaca od' if Karta.jeJaca(zog, k1, k2) else 'je slabija od'
     print('Briskula je %s, %s %s %s' % (zog, k1, poruka, k2))'''

sp=Spil()
#sp.promjesaj()
#print(sp.dajKartu(2))
#sp.izvadiZog()
print(sp)
