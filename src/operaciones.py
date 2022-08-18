#def operacion (valor1, valor2 ):
        

def run():

    menu = """
Bienvenido a tu calculadora basica

Elige una opcion

1 - para sumar
2 - para restar
3 - para dividir
4 - para multiplicar 
: """

    opcion = int (input (menu))

    valor1 = int (input ("dame el primer valor: "))
    valor2 = int (input ("dame el segundo valor: "))

    if opcion == 1: 
        suma = valor1 + valor2
        print (suma)
    elif opcion == 2:
        resta = valor1 - valor2
        print (resta)
    elif opcion == 3:
        division = valor1 // valor2
        print (division)
    elif opcion == 4:
        multipicar = valor1 * valor2
        print (multipicar)          
    else:
        print ("esa opcion no esta disponible") 


if __name__ =="__main__":
        run()
        exit("bye,bye" )   