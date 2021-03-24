import random
import numpy as np

print("Hola! Bienvenido al juego Meomorice")
numero_cartas = int(input("¿Con cuantos pares quieres jugar? "))
puntos_jugador1 = int(0)
puntos_jugador2 = int(0)
lista_tablero = []

n = 1
while n <= numero_cartas:
    lista_tablero.append(n)
    lista_tablero.append(n)
    n += 1

random.shuffle(lista_tablero)

tablero_oculto = []
tablero_numeros = []
n = int((2*numero_cartas)**(1/2))
z = 0

if (n**2) == 2*numero_cartas:

    for x in range(0,n):
        tablero_oculto_add = []

        for i in range(0,n):
            tablero_oculto_add.append("*")

        tablero_oculto.append(tablero_oculto_add)

    for a in range(0,n):
        tablero_numeros_add = []

        for b in range(0,n):
            tablero_numeros_add.append(int(lista_tablero[z]))
            z += 1

        tablero_numeros.append(tablero_numeros_add)
            
else:
    numero_filas = int((2*numero_cartas)**(1/2)) + 1
    numero_columnas = numero_filas  
    z = 0 
    
    for i in range(0,numero_filas):
        tablero_oculto_add = []

        for x in range(0, numero_columnas):

            if z < len(lista_tablero):
                tablero_oculto_add.append("*")
                z += 1

            else:
                tablero_oculto_add.append ("")
                z += 1
        
        tablero_oculto.append(tablero_oculto_add)

    z = 0

    for i in range(0,numero_filas):
        tablero_numeros_add = []

        for x in range(0, numero_columnas):

            if z < len(lista_tablero):
                tablero_numeros_add.append(int(lista_tablero[z]))
                z += 1

            else:
                tablero_numeros_add.append ("")
                z += 1

        tablero_numeros.append(tablero_numeros_add)

"""
for i in tablero_numeros:
    print(*i)
"""

n = 0

while (puntos_jugador1 + puntos_jugador2) < numero_cartas:
    puntos_jugador1_rec = puntos_jugador1
    puntos_jugador2_rec = puntos_jugador2
    n = 0

    while puntos_jugador1 != puntos_jugador1_rec or n == 0:
        print("")
        print("Player 1 turn!")
        print("")

        for i in tablero_oculto:
            print(*i)

        n = 1
        puntos_jugador1_rec = puntos_jugador1

        print("")
        columna_elegida_j11 = (int(input ("Choose a column (from 1 to n): ")) - 1)
        fila_elegida_j11 = (int(input ("Choose a row (from 1 to n): ")) - 1) 
        numero1 = tablero_numeros[fila_elegida_j11][columna_elegida_j11]
        print("")
        print("Card number: ", numero1)
        print("")
        tablero_oculto[fila_elegida_j11][columna_elegida_j11] = numero1
        for i in tablero_oculto:
            print(*i)

        print("")
        columna_elegida_j12 = (int(input ("Choose a column (from 1 to n): ")) - 1)
        fila_elegida_j12 = (int(input ("Choose a row (from 1 to n): ")) - 1) 
        numero2 = tablero_numeros[fila_elegida_j12][columna_elegida_j12]
        print("")
        print("Card number: ", numero2)
        print("")
        tablero_oculto[fila_elegida_j12][columna_elegida_j12] = numero2

        for i in tablero_oculto:
            print(*i)

        tablero_oculto[fila_elegida_j11][columna_elegida_j11] = "*"
        tablero_oculto[fila_elegida_j12][columna_elegida_j12] = "*"

        if numero1 == numero2:
            puntos_jugador1 += 1
            print("")
            print("You won a point")
            print("")
            print("Total points player1: ", puntos_jugador1)
            print("")
            tablero_oculto[fila_elegida_j11][columna_elegida_j11] = "-"
            tablero_oculto[fila_elegida_j12][columna_elegida_j12] = "-"

            if puntos_jugador1 + puntos_jugador2 == numero_cartas:
                n = 3
                break

    while puntos_jugador2 != puntos_jugador2_rec or n == 1:
        print("")
        print("Player 2 turn!")
        print("")

        for i in tablero_oculto:
            print(*i)
        
        n = 2
        puntos_jugador2_rec = puntos_jugador2

        columna_elegida_j21 = (int(input ("Choose a column (from 1 to n): ")) - 1)
        fila_elegida_j21 = (int(input ("Choose a row (from 1 to n): ")) - 1) 
        numero1 = tablero_numeros[fila_elegida_j21][columna_elegida_j21]
        print("")
        print("Card number: ", numero1)
        print("")
        tablero_oculto[fila_elegida_j21][columna_elegida_j21] = numero1

        for i in tablero_oculto:
            print(*i)

        columna_elegida_j22 = (int(input ("Choose a column (from 1 to n): ")) - 1)
        fila_elegida_j22 = (int(input ("Choose a row (from 1 to n): ")) - 1) 
        numero2 = tablero_numeros[fila_elegida_j22][columna_elegida_j22]
        print("")
        print("Card number: ", numero2)
        print("")
        tablero_oculto[fila_elegida_j22][columna_elegida_j22] = numero2

        for i in tablero_oculto:
            print(*i)

        tablero_oculto[fila_elegida_j21][columna_elegida_j21] = "*"
        tablero_oculto[fila_elegida_j22][columna_elegida_j22] = "*"

        if numero1 == numero2:
            puntos_jugador2 += 1
            print("")
            print("You won a point")
            print("")
            print("Total points player 2: ", puntos_jugador2)
            print("")
            tablero_oculto[fila_elegida_j21][columna_elegida_j21] = "-"
            tablero_oculto[fila_elegida_j22][columna_elegida_j22] = "-"

            if puntos_jugador1 + puntos_jugador2 == numero_cartas:
                break

if puntos_jugador1 > puntos_jugador2:
    print("Player 1 won!")

elif puntos_jugador1 < puntos_jugador2:
    print("Player 2 won!")

else:
    print("It's a tie!")

print("")