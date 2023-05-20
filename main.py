# Evaluación #1: Problema del Ebrio
# Diego Andrés Faria Brito (V29.714.067)
# Simulación de Sistemas (N1113)
# 
# Este archivo fuente es ejecutable dada la naturaleza
# de lenguaje interpretado de Python. Instalar Python.

from random import randint

probs = 0

for i in range(0,100): # Cien Simulaciones
    posicion_inicial = [0,0]
    for j in range(0,10): # Diez movimientos por cada uno
        numero_random = randint(0,4)

        if(numero_random == 0):
            posicion_inicial[0] += 1
        elif(numero_random == 1):
            posicion_inicial[0] += -1
        elif(numero_random == 2):
            posicion_inicial[1] += 1
        else:
            posicion_inicial[1] += -1
        
    distancia = sum([abs(x) for x in posicion_inicial])
    if(distancia == 2):
        probs += 1

print(f"La probabilidad dada en las simulaciones es la siguiente: {probs}%.")
input("Presione enter para cerrar: ")