def conversor(tipo_pesos, valor_dolar):
    pesos = float (input ("¿cuantos pesos " + tipo_pesos + " tienes?: "))
    dolares = pesos / valor_dolar
    dolares = round (dolares,2)
    dolares = str (dolares)
    print ("tienes $"+ dolares + " dolares")

menu = """
Bienvenido al conversor de moneda

1 - pesos mexicanos
2 - pesos argentinos 
3 - pesos colombianos

Elige una opción """
   
opcion = int (input (menu))
if opcion == 1:
    conversor("mexicanos", 21) 
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("colombianos", 3875)
else:
    print ("Ingresa una opción valida")