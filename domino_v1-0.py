#! python3

#programa para simular juego de dominó
#Importando librerias
import random

#Declarando todas las fichas disponibles (28 piezas):
f1= [0,0]
f2= [0,1]
f3= [0,2]
f4= [0,3]
f5= [0,4]
f6= [0,5]
f7= [0,6]
f8= [1,1]
f9= [1,2]
f10= [1,3]
f11= [1,4]
f12= [1,5]
f13= [1,6]
f14= [2,2]
f15= [2,3]
f16= [2,4]
f17= [2,5]
f18= [2,6]
f19= [3,3]
f20= [3,4]
f21= [3,5]
f22= [3,6]
f23= [4,4]
f24= [4,5]
f25= [4,6]
f26= [5,5]
f27= [5,6]
f28= [6,6]
nombresFichas = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,
                f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,f28]

#Declarando la lista principal sobre la que se desarrolla el juego 
# y las listas con las fichas de los jugadores.
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

#Algoritmo para identificar y colocar la primer ficha doble
#para comenzar la partida.
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
