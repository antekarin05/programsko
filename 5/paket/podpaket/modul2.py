# modul2.py

var2 = 2

def funkcija2():
     print('funkcija "%s" modula "%s"' % (funkcija2.__name__, __name__))

class Klasa2(object):

     def __init__(self):
          print('klasa "%s" modula "%s"' % (Klasa2.__name__, __name__))


if __name__ == "__main__":
     print("modul2.py")
     print(var2)
     funkcija2()
     objekt2 = Klasa2()
