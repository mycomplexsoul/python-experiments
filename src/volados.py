import random

print ("""          --- Juguemos valados --- 

* La computadora lanzara una moneda y tu objetibo es adivinar si cayo (cara) o (cruz)

* Comenzaras con 5 monedas, ganaras una extra por cada vez que aciertes y perderas una si fallas

* El juego acaba si te quedas sin monedas o consiges 10 monedas

* Al final de cada intento se te mostrara que eligio la computadora 

* Si en cualquer momento quieres retirarte. Escribe (salir) y el juego terminara
""")

lanzamiento = ("Elige cara o cruz: ")
eleccion = input (lanzamiento)
contador = 5

while contador != 0:
    
    # lanzamiento_computadora = random.randint(1,2)
    
    # if lanzamiento_computadora == 1:
    #     lanzamiento_computadora = "cara"
    # if lanzamiento_computadora == 2 :
    #     lanzamiento_computadora = "cruz"

    lanzamiento_computadora =("cara", "cruz")
    lanzamiento_computadora = random.choice(lanzamiento_computadora)
    
    if eleccion == "salir":
        exit ("Te quedaron "+ str(contador)+ " monedas. Estuviste cerca gracias por jugar")

    if eleccion == lanzamiento_computadora:
        contador += 1
        if contador == 10:
            exit ("Felizidades llegaste a 10 monedas ")
        else:
            print ("Ganaste, tienes: " + str(contador)+" monedas.")

    elif eleccion != lanzamiento_computadora:
        contador -= 1
        if contador == 0:
           exit("Ya no te quedan monedas")
        else:
            print ("Perdiste, tienes: "+ str(contador)+" monedas.")

    print (" La computadora eliguio " + lanzamiento_computadora)
    eleccion = input (lanzamiento)   