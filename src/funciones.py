def conversacion(mensaje):
    print ("Hola")
    print (mensaje)
    print ("Gracias y hasta luego")

opcion = int(input("Elige un opción (1,2,3): "))

if opcion == 1:
    conversacion("Elegiste la opcion 1")
elif opcion == 2:
    conversacion("Elegiste la opcion 2")     
elif opcion == 3:
    conversacion("Elegiste la opcion 3")
else:
    print("Elige un opcion valida")