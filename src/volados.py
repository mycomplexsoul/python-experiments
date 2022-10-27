import random

print ("""          --- Jugemos valados --- 

* La computadora lanzara una moneda y tu objetibo es adivinar si cayo (cara) o (cruz)

* Puedes comenzaras con un maximo de 50 monedas

* El juego acaba si te quedas sin monedas o consiges 100 monedas

* Al final de cada intento se te mostrara que eligio la computadora 

* Si en cualquer momento quieres retirarte. Escribe (salir) y el juego terminara
""")

contador = int(input ("Cuantas monedas tienes: "))
if contador > 50:
    contador = int (input("El numero de monedas no debe ser mayor a 50: "))
    while contador > 50 or contador < 0:
        if contador > 50:
            contador = int(input("Ese numero es muy grande. Pueba de nuevo: "))
        elif contador <= 0:
            contador = 5 
            print("Ya que no tienes monedas te daremos 5: ")
if contador <= 0:
    contador = 5 
    (print("Ya que no tienes monedas te daremos 5: "))

lanzamiento = ("Elige cara o cruz: ")
eleccion = input (lanzamiento)


while contador != 0:# compararlo con la cantidad actual
   
    if eleccion == "salir":
        exit ("Te quedaron "+ str(contador)+ " monedas. Estuviste cerca gracias por jugar")    
    # lanzamiento_computadora = random.randint(1,2)
    
    # if lanzamiento_computadora == 1:
    #     lanzamiento_computadora = "cara"
    # if lanzamiento_computadora == 2 :
    #     lanzamiento_computadora = "cruz"
        #agregar la opcion de que cantidad quieren apostar
    apuesta =int(input("Cuanto quieres apostar: "))  
    while apuesta >= 0:

        if apuesta >  contador:
            apuesta =  int(input("no puedes apostar mas de lo que tienes: "))

        if apuesta <= contador:
            print ("La apuesta actual es de: " +str(apuesta))
            apuesta = int(apuesta)
            break
 
    
    lanzamiento_computadora =("cara", "cruz")
    lanzamiento_computadora = random.choice(lanzamiento_computadora)
 
    if eleccion == lanzamiento_computadora:
        contador = int(contador)+(apuesta)
        if contador == 100:
            exit ("Felizidades llegaste a 100 monedas.")
        else:
            print ("Ganaste, tienes: " + str(contador)+" monedas.")

    elif eleccion != lanzamiento_computadora:
        contador = int(contador)-(apuesta)
        if contador <= 0:
           exit("Perdiste, ya no te quedan monedas")
        else:
            print ("Perdiste, tienes: "+ str(contador)+" monedas.")

    print (" La computadora eliguio " + lanzamiento_computadora)
    eleccion = input (lanzamiento)   