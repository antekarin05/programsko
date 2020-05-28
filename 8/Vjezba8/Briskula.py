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

for zog in Karta.zogovi():
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
     print('Briskula je %s, %s %s %s' % (zog, k1, poruka, k2))
