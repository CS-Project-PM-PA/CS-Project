## Input type of conversion
## Types of COnversions - length, weight, volume, imperial, currency, temperature, speed, angles
## Input VALUE
## Input SI UNIT FOR INPUT
## Input SI UNIT FOR OUTPUT
##SI INPUT / SI OUTPUT

from length import *
from weight import *
from volume import *
from currency import *
from speed import *
from angles import *
from pressure import *
from temperature import *

while True:
    print("==================================================================================================================================================")

    convert_type = input("Enter type: L(Length), W(Weight), V(Volume), C(Currency), T(Temperature), S(Speed), A(Angles), P(Pressure) \n ====>  ")

    if convert_type == "L":      
        L()
    elif convert_type == "W":
        W()
    elif convert_type == "V":
        V()
    elif convert_type == "C":
        C()
    elif convert_type == "S":
        S()
    elif convert_type == "A":
        A()
    elif convert_type == "P":
        P() 
    elif convert_type == "T":
        T()   
    else:
        print("INVALID TYPE")
        continue

