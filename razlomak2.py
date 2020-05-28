class Razlomak(object):
     '''Klasa Razlomak'''

     def __init__(self, brojnik, nazivnik = 1):
          if nazivnik == 0: raise Exception('Nazivnik ne moze biti 0')
          self._brojnik = brojnik
          self._nazivnik = nazivnik

     def __str__(self):
          return '%d|%d' % (self._brojnik, self._nazivnik)

     @staticmethod
     def inverz(self):
        return Razlomak(self._nazivnik, self._brojnik)

     @staticmethod
     def stvori(broj):
        broj_decimala = 0
        nazivnik = 10

        while (broj % 1 != 0):
            broj *= 10
            broj_decimala += 1
        nazivnik = pow(nazivnik, broj_decimala)

        return Razlomak(broj, nazivnik)


print('*** test1 ***')
r1 = Razlomak(314, 100)
r2 = Razlomak.inverz(r1)
print(r1, r2, r1)

print('*** test2 ***')
r1 = Razlomak.stvori(3.14)
print(r1)
r2 = Razlomak.stvori(0.006021)
print(r2)
r3 = Razlomak.stvori(-75.204)
print(r3)
