<<<<<<< HEAD
# ------------------------------------------------------
# ------------------- simulacion.py --------------------
# ------------------------------------------------------

# from main import *

import sys
import math
import msvcrt
import random

def Simulacion():
    dias = 31
    u = CongruencialMixto()
    P = 20000 + 10000 * u

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

    # TODO: Hacer segundo while para adelante

    u = CongruencialMixto()
    PL=u*100
    MM=0

    if u >= 0.35:
        MM=Normal(13,6.22)
        
        if MM > 16:
            TL="'LLUVIA MUY ABUNDANTE'"
        elif MM>7:
            TL="'LLUVIA INTENSA'"
        else:
            TL="'LLUVIA LIGERA'"
    else:
        TL="'NO LLUEVE'"
    
    u = CongruencialMixto()
    PH=u*100
    PL=float("{:.2f}".format(PL))
    PH=float("{:.2f}".format(PH))
    GT=float("{:.2f}".format(GT))
    if u >= 0.80:
        #HAY HURACAN
        print("Tipó de Lluvia: " + str(TL) + "Probabilidad de lluvias:: " + str(PL) +"Probabilidad de huracanes: " + str(PH) +"Perdidas Potenciales por Cierre: " + str(GT) + "Se sugiere cerrar el parque")
        return [P,PL,PH,GT]
    else:
        #NO HAY HURACAN
        print("Tipó de Lluvia: " + str(TL) + "Probabilidad de lluvias:: " + str(PL) +"Probabilidad de huracanes: " + str(PH) +"Perdidas Potenciales por Cierre: " + str(GT))
        return [P,PL,PH,GT]


def CongruencialMixto():

    listaNrosAleatorios = []
    i=0
    
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
    print("llegue hasta aqui" + str(x))
    return x

if __name__ == "__main__":
    Simulacion()
    # pass
=======
# ------------------------------------------------------
# ------------------- simulacion.py --------------------
# ------------------------------------------------------

# from main import *

import sys
import math
import msvcrt
import random

def Simulacion():
    dias = 31
    u = Lehmer(random.randint(1, 10000) , random.randint(1, 10))
    P = 20000 + 10000 * u

    i = 0 
    GT = 0
    while i <= P:
        u = Lehmer(random.randint(1, 10000) , random.randint(1, 10))
        if u >= 0.95:
            # print(">= 0.95")
            u = Lehmer(random.randint(1, 10000) , random.randint(1, 10))
            G = 100 + 400 * u
        elif u >= 0.75:
            # print("0.75 <= u < 0.95")
            u = Lehmer(random.randint(1, 10000) , random.randint(1, 10))
            G = 30 + 70 * u
        elif u >= 0.15:
            # print("0.15 <= u < 0.75")
            u = Lehmer(random.randint(1, 10000) , random.randint(1, 10))
            G = 13 + 17 * u
        else:
            # print("< 0.15")
            u = Lehmer(random.randint(1, 10000) , random.randint(1, 10))
            G = 0 + 13 * u

        # print("u: " + str(u))
        # print("G: " + str(G))

        GT += G
        i += 1 
    print("GT: " + str(GT))

    #TODO: Hacer segundo while para adelante

    u = Lehmer(random.randint(1, 10000) , random.randint(1, 10))
    PL=u*100
    MM=0
    if u >= 0.35:
        MM=17
        if MM > 16:
            TL="'LLUVIA MUY ABUNDANTE'"
        elif MM>7:
            TL="'LLUVIA INTENSA'"
        else:
            TL="'LLUVIA LIGERA'"
    else:
        TL="'NO LLUEVE'"       
    
    u = Lehmer(random.randint(1, 10000) , random.randint(1, 10))
    PH=u*100

    if u >= 0.20:
        #HAY HURACAN
        print("Tipó de Lluvia: " + str(TL) + "Probabilidad de lluvias:: " + str(PL) +"Probabilidad de huracanes: " + str(PH) +"Perdidas Potenciales por Cierre: " + str(GT) + "Se sugiere cerrar el parque")
    else:
        #NO HAY HURACAN
        print("Tipó de Lluvia: " + str(TL) + "Probabilidad de lluvias:: " + str(PL) +"Probabilidad de huracanes: " + str(PH) +"Perdidas Potenciales por Cierre: " + str(GT))
    

def Lehmer(semilla = 0, t = 0):

    listaNrosAleatorios = []
    
    # print("---------------------------------------------")
    # print("-------------- MÉTODO DE LEHMER -------------")
    # print("---------------------------------------------")

    i=0

    try:
        if semilla == 0 or t == 0:
            semilla = int(input("Ingrese la semilla n0: "))
            t = int(input("Ingrese el numero t: "))
        
        k = int(math.log10(t))+1
        n = int(math.log10(semilla))+1

        # cantNro = int(input("Cantidad de números aleatorios a generar: "))
        cantNro = 1
        while(k>n):
            print("Error. Volver a ingresar los números")
            semilla = int(input("Ingrese la semilla n0: "))
            t = int(input("Ingrese el numero t: "))
            k = int(math.log10(t))+1
            n = int(math.log10(semilla))+1

        # print("-------")
        while(i<cantNro):
            total = str(semilla*t)
            kDig = total[0:k]
            ultimos = total[k:len(total)]
            ni = int(ultimos) - int(kDig)
            if ni < 0: 
                print("No se puede generar el número u" + str(i+1))
                print("Se guardará hasta el número u" + str(i))
                print("\nPresione una tecla para continuar...")
                msvcrt.getch()
                if i == 0:
                    return random.random()
                else:
                    return listaNrosAleatorios[0]
            concatenar = "0."+str(ni)
            nroAleatorio = float(concatenar)
            listaNrosAleatorios.append(nroAleatorio)
            # print("n" + str(i+1) + " : " + str(ni))
            # print("u" + str(i+1) + " : " + concatenar)
            # print("-------")
            semilla = ni
            i = i+1
        
        # Retorna el primer numero generado
        return listaNrosAleatorios[0]
            
    except(ValueError):
        print("Tienes un error de tipo: ",sys.exc_info()[0])
        print("Nota: Se debe ingresar un valor de tipo numerico")
        return []

if __name__ == "__main__":
    # Simulacion()
    pass
>>>>>>> cf77157 (Viaje en el tiempo y Solucione un temita)
