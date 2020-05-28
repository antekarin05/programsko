import sys

for naziv_modula in sys.builtin_module_names:
     print(naziv_modula)

for direktorij in sys.path:
     print(direktorij)

#prvi nacin
#import naziv_modula

import math

print(math.sqrt(2))
print(math.log10(1000))

#drugi nacin
# import naziv_modula as alternativni_naziv
import math as matematika

print(matematika.sqrt(2))
print(matematika.log10(1000))

#treci nacin
#from naziv_modula import *
from math import *

print(sqrt(2))
print(log10(1000))

#cetvrti nacin
#from naziv_modula import id1, id2, ...
from math import sqrt, log10

print(sqrt(2))
print(log10(1000))

#peti nacin
#from naziv_modula import id1 as an1, id2 as an2, ...
from math import sqrt, log10 as logaritam

print(sqrt(2))
print(logaritam(1000))