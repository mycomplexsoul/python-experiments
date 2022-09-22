import random
    
lanzamiento_computadora = random.randint(1,2)
    
if lanzamiento_computadora == 1:
    lanzamiento_computadora = "cara"
if lanzamiento_computadora == 2 :
    lanzamiento_computadora = "cruz"

     
lanzamiento = (" Elige cara o cruz: ")
eleccion = input (lanzamiento)
contador = 5


while contador != 0:
    
    if eleccion == lanzamiento_computadora:
        contador = contador +1
        print ("ganaste: " + str(contador))
        eleccion = input (lanzamiento)
    elif eleccion != lanzamiento_computadora:
        contador = contador -1
        print ("perdiste: "+ str(contador))
        eleccion = input (lanzamiento)   
print(contador)