# modul1.py

var1 = 1

def funkcija1():
     print('funkcija "%s" modula "%s"' % (funkcija1.__name__, __name__))

class Klasa1(object):

     def __init__(self):
          print('klasa "%s" modula "%s"' % (Klasa1.__name__, __name__))


if __name__ == "__main__":
     print("modul1.py")
     print(var1)
     funkcija1()
     objekt1 = Klasa1()