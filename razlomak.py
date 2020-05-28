def main():
    pass

if __name__ == '__main__':
    main()

class Razlomak(object):

    def __init__(self, brojnik, nazivnik):
        self.brojnik = brojnik
        self.nazivnik = nazivnik

    def getBrojnik(self):
        return self.brojnik

    def setBrojnik(self, value):
        self.brojnik = value

    def getNazivnik(self):
        return self.nazivnik

    def setNazivnik(self, value):
        self.nazivnik = value

    def skrati(self):
        brojnik = self.brojnik
        nazivnik = self.nazivnik
        while brojnik % nazivnik != 0:
            brojnik, nazivnik = nazivnik, brojnik % nazivnik
        r1 = nazivnik
        self.brojnik //=r1
        self.nazivnik //=r1
        return
print('*** test 1 ***')
r1 = Razlomak(12,30)
print(r1.brojnik, r1.nazivnik)
r1.skrati()
print(r1.brojnik, r1.nazivnik)



class Razlomak(object):

    def __init__(self, brojnik, nazivnik):
        self._brojnik = brojnik
        self.nazivnik = nazivnik

    @property
    def brojnik(self):
        return self._brojnik

    @brojnik.setter
    def brojnik(self, value):
        self._brojnik = value

    @property
    def nazivnik(self):
        return self._nazivnik

    @nazivnik.setter
    def nazivnik(self, value):
        self._nazivnik = value

    @property
    def razlomak(self):
        return self.brojnik / self.nazivnik

    def __repr__(self):
        return "Razlomak ("+repr(self._brojnik)+ ',' + repr(self._nazivnik)+ ")"

    def __str__(self):
        return str(self._brojnik) + '|' + str(self._nazivnik)

    def __eq__(self, other):
        return self.razlomak == other.razlomak

    def __lt__(self,other):
        return self.razlomak < other.razlomak

    def __le__(self,other):
        return self.razlomak <= other.razlomak

    def __add__(self, other):
        return Razlomak(self.brojnik*other.nazivnik+self.nazivnik*other.brojnik,
                        self.nazivnik*other.nazivnik)

    def __sub__(self, other):
        return Razlomak(self.brojnik*other.nazivnik-self.nazivnik*other.brojnik,
                        self.nazivnik*other.nazivnik)

    def __mul__(self, other):
        return Razlomak(self.brojnik*other.brojnik,self.nazivnik*other.nazivnik)

    def __truediv__(self, other):
        return Razlomak(self.brojnik*other.nazivnik,self.nazivnik*other.brojnik)

print('*** test2 ***')
r1 = Razlomak(12,30)
r2 = Razlomak(2,5)
r3 = Razlomak(3,6)
print(r1,r2,repr(r3))
print(r1 == r2)
print(r3 >= r1)
print(r3 < r2)


print('*** test 3 ***')
print(Razlomak(3,4) + Razlomak(5,2))
print(Razlomak(1,3) - Razlomak(2,6))
print(Razlomak(2,8) * Razlomak(4,2))
print(Razlomak(2,3)/Razlomak(4,5))
