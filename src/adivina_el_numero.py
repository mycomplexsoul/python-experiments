import random

def run():
    numero_aleatoreo = random.randint (1, 100)
    numero = int(input("Elige un numero del uno al 100: "))
    while numero != numero_aleatoreo:
        if numero < numero_aleatoreo:
            print("busca un numero mas grande: ")
        else:
            print("busca un numero mas pequeño: ")
        numero =int(input("Escribe otro numero: "))
    print("¡Ganaste!")


if __name__=="__main__":
    run () 