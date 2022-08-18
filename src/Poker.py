import random
#falta implementar las partes mas importante( las reglas del poker)
#es mejor hacer una lista de numeros y luego agregar los simbolos
def mazo_de_cartas():
    CORAZONES = ['♥1','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥11','♥12']
    TREBOLES = ['♣1','♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣11','♣12']
    DIAMANTES =['♦1','♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦10','♦11','♦12']
    ESPADAS = ['♠1','♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠11','♠12']
    
    mazo = CORAZONES + TREBOLES + DIAMANTES + ESPADAS
    mano_jugador = []
    #mano_computadora = []
    #poso = [] #agregar un contador para el poso (3 + 1==5)¿o deberia ser 6?

    for i in range(2):
        carta_ramdon = random.choice(mazo)
        mano_jugador.append(carta_ramdon)

    mano_jugador = '' .join(mano_jugador)
    return mano_jugador
#tengo que encontrar la forma de que un numero que ya salio no se repita

    #for x in range(2):
    #    carta_ramdon1 = random.choice(mazo)
    #    mano_computadora.append(carta_ramdon1)

    #mano_computadora = ''.join(mano_computadora)
    #return mano_computadora
#poso debe llevar un ciclo whille que comiense en 3 y termine en 5 o 6
    #for y in range(5):
    #    carta_ramdon2 = random.choice(mazo)
    #    poso.append(carta_ramdon2)
    #poso = ''.join(poso)
    #return poso


def run():
    mano_jugador = mazo_de_cartas
    #mano_computadora = mazo_de_cartas
    #poso = mazo_de_cartas
    print('tu mano es:'+ mano_jugador) #+ mano_computadora + poso)

if __name__=="__main__":
    run
#...
# ¿¿¿COMO VOY A PROGRAMAR EL SISTEMA QUE DEFINA AL GANADOR???...
# talves tenga que terminar despues