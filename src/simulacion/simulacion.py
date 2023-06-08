# ------------------------------------------------------
# ------------------- simulacion.py --------------------
# ------------------------------------------------------

# from main import *

import sys
import math
import msvcrt

def Simulacion():
    dias = 31
    u = Lehmer(2546, 5)
    P = 20000 + 10000 * u

    i = 0 
    GT = 0
    while i <= P:
        u = Lehmer(9999, 9)
        if u >= 0.95:
            # print(">= 0.95")
            u = Lehmer(232,4)
            G = 100 + 400 * u
        elif u >= 0.75:
            # print("0.75 <= u < 0.95")
            u = Lehmer(232,4)
            G = 30 + 70 * u
        elif u >= 0.15:
            # print("0.15 <= u < 0.75")
            u = Lehmer(232,4)
            G = 13 + 17 * u
        else:
            # print("< 0.15")
            u = Lehmer(232,4)
            G = 0 + 13 * u

        # print("u: " + str(u))
        # print("G: " + str(G))

        GT += G
        i += 1 
    print("GT: " + str(GT))

    #TODO: Hacer segundo while para adelante

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
                return listaNrosAleatorios
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


Simulacion()