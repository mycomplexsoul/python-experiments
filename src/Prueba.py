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
    
movimientos="""
Escribe 1 para mover el (numero mas alto) a la primer linea.
Escribe 2 para mover el (numero mas alto) a la segunda linea. 
Escribe 3 para mover el (numero mas alto) a la tercer linea
Escribe 4 para mover el (siguiente numero) a la primer linea
Escribe 5 para mover el (siguiente numero) a la seunda linea
Escribe 6 para mover el (siguiente numero) a la tercer linea
:"""


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
    
print(lineaA,lineaB,lineaC)


mover = int(input(movimientos)) 
    #Bucle
#while linea3.length == discos:
while mover == 1 or mover == 2 or mover == 3:

    # determinar que discos se pueden mover
    # los discos que se pueden mover son los que están al final de cada linea (maximo se pueden mover 3 discos)
    lenA = len(lineaA)
    lenB = len(lineaB)
    lenC = len(lineaC)

    discosQueSePuedenMover = list(range(1, (1 if lenA > 0 else 0) + (1 if lenB > 0 else 0) + (1 if lenC > 0 else 0) ))
    #def movvmientosposibles()
    movimientosPosibles = {}
    if lenA > 0:
        discosQueSePuedenMover[0] = [lineaA[len(lineaA) - 1]]

    if lenB > 0:
        discosQueSePuedenMover[1] = [lineaB[len(lineaB) - 1]]
    
    if lenC > 0:
        discosQueSePuedenMover[2] = [lineaC[len(lineaC) - 1]]

    # para cada disco, determinar que movimientos es posible realizar
    if lenA > 0:
        movimientosPosibles[str(discosQueSePuedenMover[0])] = []
        
        if lenB > 0 and discosQueSePuedenMover[0] > discosQueSePuedenMover[1]:
            movimientosPosibles[str(discosQueSePuedenMover[0])].append('B')
        
        if lenC > 0 and discosQueSePuedenMover[0] > discosQueSePuedenMover[2]:
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

    # Idea de función para determinar movimientos posibles
    def determinaMovimientosPosibles(lenA, lenB, lenC, discosQueSePuedenMover, disco): #disco = 0, 1, 2
        if disco == 0:
            len = lenA
            lenNoUsado1 = lenB
            lenNoUsado2 = lenC
            discoNoUsado1 = 1
            discoNoUsado2 = 2
            lineaNoUsada1 = 'B'
            lineaNoUsada2 = 'C'
        elif disco == 1:
            len = lenB
            # TODO
        elif disco == 2:
            len = lenC
            # TODO

        if len > 0:
            movimientosPosibles[str(discosQueSePuedenMover[disco])] = []
            
            if lenNoUsado1 > 0 and discosQueSePuedenMover[disco] > discosQueSePuedenMover[discoNoUsado1]:
                movimientosPosibles[str(discosQueSePuedenMover[disco])].append(lineaNoUsada1)
            
            if lenNoUsado2 > 0 and discosQueSePuedenMover[disco] > discosQueSePuedenMover[discoNoUsado2]:
                movimientosPosibles[str(discosQueSePuedenMover[disco])].append(lineaNoUsada2)

    # determinaMovimientosPosibles(lenA, lenB, lenC, discosQueSePuedenMover, 0)
    # determinaMovimientosPosibles(lenA, lenB, lenC, discosQueSePuedenMover, 1)
    # determinaMovimientosPosibles(lenA, lenB, lenC, discosQueSePuedenMover, 2)

    if mover == 2:
        lineaB.append (lineaA.pop())
        print(lineaA,lineaB,lineaC)
        movimiento = int(input(movimientos))
        while movimiento  > 1 or movimiento  < 6:
            if movimiento == 1:
                lineaA.append (lineaB.pop())
                print(lineaA,lineaB,lineaC)
                movimiento = int(input(movimientos))
                while movimiento  > 1 or movimiento  < 6:
                    if movimiento == 2:
                        lineaB.append (lineaA.pop())
                        print(lineaA,lineaB,lineaC)
                        movimiento = int(input(movimientos))
                    elif movimiento == 3:
                        continue
                    elif movimiento == 1:
                        movimiento = int (input ("Este movimiento no puede realizarce actual mente,por favor intente con otro.")) 
                    elif movimiento > 4 or movimiento < 6:
                        movimiento = int (input ("Este movimiento no puede realizarce actual mente,por favor intente con otro."))
                    else:
                        movimiento =int (input ("Por favor,escribe una opcion valida:"))       
            elif movimiento == 3:
                lineaC.append (lineaB.pop())
                print(lineaA,lineaB,lineaC)
                movimiento = int(input(movimientos))
                while movimiento  > 1 or movimiento  < 6:
                    if movimiento == 1:
                        lineaA.append (lineaC.pop())
                        print(lineaA,lineaB,lineaC)
                        movimiento = int(input(movimientos))
                    elif movimiento == 2:
                        reversed
                    elif movimiento == 4:
                        lineaB.append (lineaA.pop())
                        print(lineaA,lineaB,lineaC)
                        movimiento = int(input(movimientos))
                    elif movimiento == 3:
                        movimiento = int (input ("Este movimiento no puede realizarce actual mente,por favor intente con otro.")) 
                    elif movimiento > 5 or movimiento < 6:
                        movimiento = int (input ("Este movimiento no puede realizarce actual mente,por favor intente con otro."))
                    else:
                        movimiento =int (input ("Por favor,escribe una opcion valida:"))      
            elif movimiento == 2:
                movimiento = int (input ("Este movimiento no puede realizarce actual mente,por favor intente con otro."))
            elif movimiento > 4 or movimiento < 6:
                movimiento = int (input ("Este movimiento no puede realizarce actual mente,por favor intente con otro."))
            else:
                movimiento =int (input ("Por favor,escribe una opcion valida:"))
    elif mover == 3:
        lineaC.append (lineaA.pop())
        print(lineaA,lineaB,lineaC)
    elif mover == 1:
        mover = int (input ("Este movimiento no puede realizarce actual mente,por favor intente con otro."))
    else :
        mover = int (input ("Por favor,escribe una opcion valida:"))
        # Mostrar movimientos posibles con el estado actual
        ## Posibles movimientos: 1 a 2, 1 a 3
        ## Posibles movimientos [1, 2, 3] [4] []: 1 a 3, 2 a 3, 2 a 1
        ## Posibles movimientos [1, 2, 3] [] [4]: 1 a 2, 3 a 2, 3 a 1

        # Pedir input del jugador sobre que movimiento realizar
        ## Elegir movimiento:
        ## 1) Mover disco de línea 1 a 2
        ## 2) Mover disco de línea 1 a 3
        ## > 1

        # Aplicar el movimiento en las lineas
        ## si eligio 1:
            ## disco = linea1.pop()
            ## linea2 = linea2.append(disco)
        ## si eligio 2:
            ## disco = linea1.pop()
            ## linea3 = linea3.append(disco)

        # Determinar si tras realizar el movimiento el juego ha terminado o no
        ## linea3.length == discos
        ## Si el juego termino, salimos del bucle y avisamos que terminó el juego

        # Mostrar el estado del juego tras el último movimiento
    
exit (print (lineaA, lineaB, lineaC))
       
    # linea1 = ["(A)"+" "+  "1","2","3"]
    # linea2 = ["(B)"+" "+ ""]
    # linea3 = ["(C)"+" "+ ""]
    #  
    # while linea3 == ["(C)"+" "+  "1","2","3"]:
    #     if linea1 ==["(A)"+" "+  "1","2","3"]:
    #         linea3.append (linea1.pop)
    #         print (linea1, linea2, linea3)
    #     elif linea3 ==["(C)"+" "+ "3"] and linea2==["(B)"+" "+""] and linea1==["(A)"+" "+ "1","2"]:
    #         linea2.append (linea1.pop)
    #         print (linea1, linea2, linea3)
    #     elif linea3 ==["(C)"+" "+ "3"] and linea2 ==["(B)"+" "+ "2"] and linea1==["(A)"+" "+ "1"]:
    #         linea2.append (linea3.pop())
    #         print (linea1, linea2, linea3)
    #     elif linea3 ==["(C)"+" "+ ""] and linea2 ==["(B)"+" "+ "2","3"] and linea1==["(A)"+" "+ "1"]:
    #         linea3.append (linea1.pop())
    #         print (linea1, linea2, linea3)
    #     elif linea3 ==["(C)"+" "+ "1"] and linea2 ==["(B)"+" "+ "2","3"] and linea1 ==["(A)"+" "+ ""]:
    #         linea1.append (linea2.pop())
    #         print (linea1, linea2, linea3)
    #     elif linea3 ==["(C)"+" "+ "1"] and linea2 ==["(B)"+" "+ "2"] and linea1 ==["(A)"+" "+""]:
    #         linea3.append (linea2.pop())
    #         print (linea1, linea2, linea3)
    #     elif linea3 ==["(C)"+" "+ "1","2"] and linea2 ==["(B)"+" "+""] and linea1 ==["(A)"+" "+ "3"]:
    #         linea3.append (linea1.pop())
    #         print (linea1, linea2, linea3)
    #     else:
    #         print("movimiento no permitido")
# linea3.append (linea1.pop())
# linea2.append (linea1.pop())
# linea2.append (linea3.pop())
# linea3.append (linea1.pop())
# linea1.append (linea2.pop())
# linea3.append (linea2.pop())
# linea3.append (linea1.pop())
