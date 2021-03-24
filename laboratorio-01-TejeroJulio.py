import random

print("Hola! Bienvenido al juego Meomorice")
numero_cartas = int(input("¿Con cuantos pares quieres jugar?"))
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

            tablero_numeros_add.append(lista_tablero[z])
            z += 1

        tablero_numeros.append(tablero_numeros_add)
            
else:

    numero_filas = int((2*numero_cartas)**(1/2))
    numero_columnas = numero_filas + 1  
    
    for i in range(0,numero_filas):

        tablero_oculto_add = []

        for x in range(0, numero_columnas):

            if z < len(lista_tablero):

                tablero_oculto_add.append("*")
                z += 1

            else:

                tablero_oculto_add.append ("")
                z += 1
    
    z = 0

    for i in range(0,numero_filas):

        tablero_numeros_add = []

        for x in range(0, numero_columnas):

            if z < len(lista_tablero):

                tablero_numeros_add.append(lista_tablero[z])

                z += 1

            else:

                tablero_numeros_add.append ("")
                z += 1

        
        tablero_numeros.append(tablero_numeros_add)

print(tablero_numeros)