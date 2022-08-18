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
    
numero_discos ="""
    
Escrie el numero de discos con los que quieres jugar 
    ...... ¡¡¡ (NO MAYOR A 7 O MENOR A 3) !!! ......
                             """
    
discos = int (input (numero_discos))
    
while discos < 7 and discos > 3:
    if discos > 7:
        discos = int (input("El numero de discos debe ser mayor a 7: "))
        while discos > 7:
            if discos > 7:
                 discos = int(input("Ese numero es muy grande. Pueba de nuevo: "))
            else:
                discos = str (discos)
                print (("tienes") + " " + (discos) + " " + ("discos")) 
    elif discos < 3:
        discos = int (input("El numero de discos debe ser mayor a 3: "))
        while discos < 3:
            if discos < 3:
                discos = int (input("Ese numero muy pequeño. prueba de nuevo: "))
            else:
                discos = str (discos)
                print (("tienes") + " " + (discos) + " " + ("discos"))
    else:
        discos = str(discos)
        print (("tienes") + " " + (discos) + " " + ("discos")) 
        
    discos=int(discos)


    linea1 = list(range(1,discos+1))
    linea2 = []
    linea3 = []

    #Bucle
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
    
    exit (print (linea1, linea2, linea3))
       
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
