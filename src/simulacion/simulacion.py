# ------------------------------------------------------
# ------------------- simulacion.py --------------------
# ------------------------------------------------------

# from main import *

# import sys
# import math
# import msvcrt
import random

def Simulacion():
    # dias = 31
    u = CongruencialMixto()
    P = int(20000 + 10000 * u)

    i = 0 
    GT = 0
    while i <= P:
        u = CongruencialMixto()
        if u >= 0.95:
            # print(">= 0.95")
            u = CongruencialMixto()
            G = 100 + 400 * u
        elif u >= 0.75:
            # print("0.75 <= u < 0.95")
            u = CongruencialMixto()
            G = 30 + 70 * u
        elif u >= 0.15:
            # print("0.15 <= u < 0.75")
            u = CongruencialMixto()
            G = 13 + 17 * u
        else:
            # print("< 0.15")
            u = CongruencialMixto()
            G = 0 + 13 * u

        # print("u: " + str(u))
        # print("G: " + str(G))

        GT += G
        i += 1 
    print("GT: " + str(GT))

    u = CongruencialMixto()
    PL=u
    MM=0

    if u >= 0.35:
        MM=Normal(13,6.22)
        
        if MM > 16:
            TL="LLUVIA MUY ABUNDANTE"
        elif MM>7:
            TL="LLUVIA INTENSA"
        else:
            TL="LLUVIA LIGERA"
    else:
        TL="NO LLUEVE"       
    
    u = CongruencialMixto()
    PH=u
    PL=float("{:.4f}".format(PL))
    PH=float("{:.4f}".format(PH))
    GT=float("{:.4f}".format(GT))
    if u >= 0.20:
        #HAY HURACAN
        print("\nTipo de Lluvia: " + str(TL) + "\nProbabilidad de lluvias:: " + str(PL) +"\nProbabilidad de huracanes: " + str(PH) +"\nPerdidas Potenciales por Cierre: " + str(GT) + "\nSe sugiere cerrar el parque")
    else:
        #NO HAY HURACAN
        print("\nTipo de Lluvia: " + str(TL) + "\nProbabilidad de lluvias:: " + str(PL) +"\nProbabilidad de huracanes: " + str(PH) +"\nPerdidas Potenciales por Cierre: " + str(GT))
    
    return [P,PL,TL,PH,GT]


def CongruencialMixto():
    
    semilla = random.randint(1, 100)
    a = random.randint(1, 100)
    c = random.randint(1, 100)
    m = random.randint(1, 100)

    ni = (a*semilla+c)%m
    nroAleatorio = float(ni/m)

    return nroAleatorio

def Normal(m,d):
    sum=0
    i=0
    while i<12:
        u = CongruencialMixto()
        
        sum=sum+u
        i=i+1
    x = d * (sum-6) + m
    # print("llegue hasta aqui" + str(x))
    return x

if __name__ == "__main__":
    # Simulacion()
    pass