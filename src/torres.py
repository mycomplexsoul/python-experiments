turotial ="""

¿CUAL ES EL OBJETIVO DEL JUEGO? 

-El objetivo de juego es pasar todos los discos de la primer linea a la ultima en el mismo orden
                           ____|\                     
...._| |_....| |...| |...        \  ....| |....| |...._| |_...
...(_| |_)...| |...| |...  ____  /  ....| |....| |...(_| |_)..
__(__|_|__)__|_|___|_|___      |/   ____|_|____|_|__(__|_|__)_

                ***LAS REGLAS DEL JUEGO***

1- Solo puedes mover un disco a la vez.
                                                          ....../.
...._| |_....| |...| |...     ....| |....| |....| |...    ...../..
...(_| |_)...| |...| |...     ..__| |__..| |..._| |_..    .\../...
__(__|_|__)__|_|___|_|___     _(__|_|__)_|_|__(_|_|_)_    ..\/....

2- Un disco mas pequeño no puede ir despues de uno mas grande.
                                                          ..\  /..   
...._| |_....| |...| |...     ....| |....| |..__| |__..   ...\/...
...(_| |_)...| |...| |...     ....| |....| |.(__| |__).   .../\...
__(__|_|__)__|_|___|_|___     ____|_|____|_|__(_|_|_)__   ../  \..

3- Los discos estaran representados por numeros (1,2) y las lineas por el siguiente simbolo []
     []      []     []
                                            
...._| |_....| |...| |...     
...(_|2|_)...| |...| |...    [1,2] [] []
__(__|1|__)__|_|___|_|___    

4- Para realizar un movimiento, porfavor sigue las instrucciones de la consola 

si desea empezar a jugar escriba:
          (continuar)

si desea salir del juego escriba:
             (salir) 
"""

Menu = """
.....¡¡¡ Bienvenido a Torres de hanoi !!!.....
                                   
......._| |_..........| |...........| |.......
......(_| |_).........| |...........| |.......
.....(__| |__)........| |...........| |.......
____(___|_|___)_______|_|___________|_|_______

-¿conoces las reglas del juego? si/no
-Para salir del juego escriba (salir)
"""

opcion = input (Menu)
while opcion =="si" or "no" or "salir":
    if opcion == "no":
        input (turotial)
        while turotial == "continuar" or "salir":
            if turotial == "continuar":
               from Prueba import *
               break
            elif turotial == "salir":
                exit("Vuelve pronto:")
            else:
                turotial = input ("Confirma tu respuesta:")
    elif opcion == "si":
        from Prueba import *
        break
    elif opcion == "salir":
        exit("Vuelve pronto:")
    else:
        opcion = input("Esa opcion no el valida. por favor escriba (si),(no),(salir):")