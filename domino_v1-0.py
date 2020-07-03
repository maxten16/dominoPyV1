#! python3

#programa para simular juego de dominó-------------------------------------------------------------
#Importando librerias------------------------------------------------------------------------------
import random

#Declarando todas las fichas disponibles (28 piezas):
f1, f2, f3, f4, f5, f6, f7, f8, f9  = [0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6], [1,1], [1,2]
f10, f11, f12, f13, f14, f15, f16, f17 = [1,3], [1,4], [1,5], [1,6], [2,2], [2,3], [2,4], [2,5]
f18, f19, f20, f21, f22, f23, f24, f25 = [2,6], [3,3], [3,4], [3,5], [3,6], [4,4], [4,5], [4,6]
f26, f27, f28 = [5,5], [5,6], [6,6]

nombresFichas = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,
                f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,f28]

#Declarando la lista principal sobre la que se desarrolla el juego --------------------------------
# y las listas con las fichas de los jugadores.----------------------------------------------------
juego = []
fichasJugador = []
fichasPython = []

jugador = input("¿Cómo te llamas?: ")
print("Muy bien " + jugador + " yo soy Python, comencemos a jugar.")

#Reparto para el jugador
reparto = 0
while reparto < 7:
    selector = random.randint(0,27)
    if nombresFichas[selector] not in fichasJugador:
        if nombresFichas[selector] not in fichasPython:
            fichasJugador.append(nombresFichas[selector])
            reparto += 1
        else:
            continue
    else:
        continue

#Reparto para la IA
while reparto < 14:
    selector = random.randint(0,27)
    if nombresFichas[selector] not in fichasJugador:
        if nombresFichas[selector] not in fichasPython:
            fichasPython.append(nombresFichas[selector])
            reparto += 1
        else:
            continue
    else:
        continue

print("Tus fichas son: " + str(fichasJugador))
print("Mis fichas son: " + str(fichasPython))

#Climax del juego
print("\nColocando la primer ficha, después mueves tu :)")

#Algoritmo para identificar y colocar la primer ficha doble----------------------------------------
#para comenzar la partida.-------------------------------------------------------------------------
n=6
prueba = False
while prueba == False and n >= 0:
    for itemJugador in fichasJugador:
        if itemJugador == [n,n] and prueba == False:
            juego.append([n,n])
            fichasJugador.remove(itemJugador)
            print("Tus fichas son: " + str(fichasJugador))
            print("Mis fichas son: " + str(fichasPython))
            prueba = True
            break
        else:
            pass

    for itemIa in fichasPython:
        if itemIa == [n,n] and prueba == False:
            juego.append([n,n])
            fichasPython.remove(itemIa)
            print("Tus fichas son: " + str(fichasJugador))
            print("Mis fichas son: " + str(fichasPython))
            prueba = True
            break
        else:
            pass
    n -= 1
print("Primera movida "+ str(juego))

# Se define primer turno jugador o IA--------------------------------------------------------------
turnoJugador = False
turnoIA = False
finJuego = False

# Con base en quien puso primero se determina quien es el siguiente en mover-----------------------
if len(fichasPython) < len(fichasJugador):
    turnoJugador = True
else:
    turnoIA = True

# Comienzan a mover los jugadores------------------------------------------------------------------
# El numero de ficha se selecciona de izquierda a derecha empezando desde el 0
while finJuego == False:
    if turnoJugador == True:
        fichaEscogidaJug = int(input("Numero de ficha: "))
        if fichaEscogidaJug >= 0 and fichaEscogidaJug < len(fichasJugador):
            pass 
        else:
            print("Error, número inválido de ficha")
            continue
    else:
        pass