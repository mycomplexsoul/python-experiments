# def mover (n,inicio,final,paso):
    
#     if n > 0:
#         mover (n-1, inicio, paso, final)
#         final.append (inicio.pop())
#         mover (n-1, paso, final, inicio)

# n = 3
# A = range(n,0,-1)
# B = []
# C = []
# print (A, B, C)
# mover (n, A, C, B)
# print (A, B, C)

#def game ():
    
# movimientos="""
# Escribe 1 para mover el (numero mas alto) a la primer linea.
# Escribe 2 para mover el (numero mas alto) a la segunda linea. 
# Escribe 3 para mover el (numero mas alto) a la tercer linea
# Escribe 4 para mover el (siguiente numero) a la primer linea
# Escribe 5 para mover el (siguiente numero) a la seunda linea
# Escribe 6 para mover el (siguiente numero) a la tercer linea
# :"""


numero_discos ="""
    
Escrie el numero de discos con los que quieres jugar 
    ...... ¡¡¡ (NO MAYOR A 7 O MENOR A 3) !!! ......
                             """
    
discos = int (input (numero_discos))
    
#while discos < 7 or discos > 3:
if discos > 7:
    discos = int (input("El numero de discos debe ser mayor a 7: "))
    while discos > 7 or discos < 3:
        if discos > 7:
            discos = int(input("Ese numero es muy grande. Pueba de nuevo: "))
        elif discos < 3:
            discos = int (input("Ese numero muy pequeño. prueba de nuevo: "))
        else:
            discos = str (discos)
            print (("tienes") + " " + (discos) + " " + ("discos")) 
if discos < 3:
    discos = int (input("El numero de discos debe ser mayor a 3: "))
    while discos < 3 or discos > 7:
        if discos < 3:
            discos = int (input("Ese numero muy pequeño. prueba de nuevo: "))
        elif discos > 7:
            discos = int(input("Ese numero es muy grande. Pueba de nuevo: "))
        else:
            discos = str (discos)
            print (("tienes") + " " + (discos) + " " + ("discos"))
else:
    discos = str(discos)
    print (("tienes") + " " + (discos) + " " + ("discos")) 
        
discos=int(discos)


lineaA = list(range(1,discos+1))
lineaB = []
lineaC = []
    
#print(lineaA,lineaB,lineaC)


# mover = int(input(movimientos)) 
#     #Bucle
# #while linea3.length == discos:
# while mover == 1 or mover == 2 or mover == 3:

# determinar que discos se pueden mover
# los discos que se pueden mover son los que están al final de cada linea (maximo se pueden mover 3 discos)
lenA = len(lineaA)
lenB = len(lineaB)
lenC = len(lineaC)
discosQueSePuedenMover = list(range(1, 4))
movimientosPosibles = {}

def calculaEstadoDelJuego(lineaA, lineaB, lineaC, discosQueSePuedenMover, movimientosPosibles):
    lenA = len(lineaA)
    lenB = len(lineaB)
    lenC = len(lineaC)

    discosQueSePuedenMover = list(range(1, 4))

    if lenA > 0:
        discosQueSePuedenMover[0] = lineaA[len(lineaA) - 1]
    else:
        discosQueSePuedenMover[0] = 0

    if lenB > 0:
        discosQueSePuedenMover[1] = lineaB[len(lineaB) - 1]
    else:
        discosQueSePuedenMover[1] = 0

    if lenC > 0:
        discosQueSePuedenMover[2] = lineaC[len(lineaC) - 1]
    else:
        discosQueSePuedenMover[2] = 0

    # para cada disco, determinar que movimientos es posible realizar
    if lenA > 0:
        movimientosPosibles[str(discosQueSePuedenMover[0])] = []
        
        if (lenB == 0) or (lenB > 0 and discosQueSePuedenMover[0] > discosQueSePuedenMover[1]):
            movimientosPosibles[str(discosQueSePuedenMover[0])].append('B')
        
        if (lenC == 0) or (lenC > 0 and discosQueSePuedenMover[0] > discosQueSePuedenMover[2]):
            movimientosPosibles[str(discosQueSePuedenMover[0])].append('C')

    if lenB > 0:
        movimientosPosibles[str(discosQueSePuedenMover[1])] = []
        
        if lenA > 0 and discosQueSePuedenMover[1] > discosQueSePuedenMover[0]:
            movimientosPosibles[str(discosQueSePuedenMover[1])].append('A')
        
        if lenC > 0 and discosQueSePuedenMover[1] > discosQueSePuedenMover[2]:
            movimientosPosibles[str(discosQueSePuedenMover[1])].append('C')

    if lenC > 0:
        movimientosPosibles[str(discosQueSePuedenMover[2])] = []
        
        if lenA > 0 and discosQueSePuedenMover[2] > discosQueSePuedenMover[0]:
            movimientosPosibles[str(discosQueSePuedenMover[2])].append('A')
        
        if lenB > 0 and discosQueSePuedenMover[2] > discosQueSePuedenMover[1]:
            movimientosPosibles[str(discosQueSePuedenMover[2])].append('B')
    
    return discosQueSePuedenMover
# Idea de función para determinar movimientos posibles
# def determinaMovimientosPosibles(lenA, lenB, lenC, discosQueSePuedenMover, disco): #disco = 0, 1, 2
#     if disco == 0:
#         len = lenA
#         lenNoUsado1 = lenB
#         lenNoUsado2 = lenC
#         discoNoUsado1 = 1
#         discoNoUsado2 = 2
#         lineaNoUsada1 = 'B'
#         lineaNoUsada2 = 'C'
#     elif disco == 1:
#         len = lenB
#         # TODO
#     elif disco == 2:
#         len = lenC
#         # TODO

#     if len > 0:
#         movimientosPosibles[str(discosQueSePuedenMover[disco])] = []
        
#         if lenNoUsado1 > 0 and discosQueSePuedenMover[disco] > discosQueSePuedenMover[discoNoUsado1]:
#             movimientosPosibles[str(discosQueSePuedenMover[disco])].append(lineaNoUsada1)
        
#         if lenNoUsado2 > 0 and discosQueSePuedenMover[disco] > discosQueSePuedenMover[discoNoUsado2]:
#             movimientosPosibles[str(discosQueSePuedenMover[disco])].append(lineaNoUsada2)

# determinaMovimientosPosibles(lenA, lenB, lenC, discosQueSePuedenMover, 0)
# determinaMovimientosPosibles(lenA, lenB, lenC, discosQueSePuedenMover, 1)
# determinaMovimientosPosibles(lenA, lenB, lenC, discosQueSePuedenMover, 2)

def muestraQueDiscosSePuedenMover(discos):
    mensaje = ''
    for disco in discos:
        mensaje = mensaje + '\r\nSe puede mover el disco: ' + str(disco)
    print(mensaje)

def muestraAQueLineasSePuedenMover(movimientosPosibles, disco):
    mensaje = ''
    for linea in movimientosPosibles[str(disco)]:
        mensaje = mensaje + '\r\nSe puede mover a la linea: ' + linea
    print(mensaje)

def aplicaMovimiento(disco, linea, lineaA, lineaB, lineaC):
    lineaOrigen = []

    if disco in lineaA:
        lineaOrigen = lineaA
    if disco in lineaB:
        lineaOrigen = lineaB
    if disco in lineaC:
        lineaOrigen = lineaC

    if linea == 'A':
        lineaA.append(lineaOrigen.pop())
    if linea == 'B':
        lineaB.append(lineaOrigen.pop())
    if linea == 'C':
        lineaC.append(lineaOrigen.pop())

discosQueSePuedenMover = calculaEstadoDelJuego(lineaA, lineaB, lineaC, discosQueSePuedenMover, movimientosPosibles)

while len(movimientosPosibles) > 0:
    discosQueSePuedenMover = calculaEstadoDelJuego(lineaA, lineaB, lineaC, discosQueSePuedenMover, movimientosPosibles)
    print(lineaA,lineaB,lineaC)
    muestraQueDiscosSePuedenMover(discosQueSePuedenMover)
    discoAMover = int(input('Escoge un disco: '))
    muestraAQueLineasSePuedenMover(movimientosPosibles, discoAMover)
    lineaADondeSeVaAMover = input('Escoge a donde mover el disco: ')

    aplicaMovimiento(discoAMover, lineaADondeSeVaAMover, lineaA, lineaB, lineaC)

    if lineaC == list(range(1,discos+1)):
        break

print(lineaA, lineaB, lineaC)
print('se acabo el juego, no hay más movimientos posibles')
