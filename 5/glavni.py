# glavni.py

'''import modul1

if __name__ == "__main__":
     print("glavni.py")
     print(modul1.var1)
     modul1.funkcija1()
     objekt1 = modul1.Klasa1()

import modul1 as m1

if __name__ == "__main__":
     print("glavni.py")
     print(m1.var1)
     m1.funkcija1()
     objekt1 = m1.Klasa1()'''

'''from modul1 import *

try:
     print(var1)
except Exception as e:
     print(e)

try:
     funkcija1()
except Exception as e:
     print(e)

try:
     objekt1 = Klasa1()
except Exception as e:
     print(e)'''

'''from modul1 import funkcija1, Klasa1 as MojaKlasa

try:
     print(var1)
except Exception as e:
     print(e)

try:
     funkcija1()
except Exception as e:
     print(e)

try:
     objekt1 = MojaKlasa()
except Exception as e:
     print(e)'''


import paket.modul1
import paket.podpaket.modul2 as m2

print(paket.modul1.var1)
paket.modul1.funkcija1()
m2.funkcija2()