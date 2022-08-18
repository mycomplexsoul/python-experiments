value = int(input('''
                  hola
                 
         ──────▄▀▄─────▄▀▄
         ─────▄█░░▀▀▀▀▀░░█▄
         ─▄▄──█░░░░░░░░░░░█──▄▄
         █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█
         
Bienvenido a catculator donde obtendras las 
tablas de multiplicar del número que desees

A continueción ingresa un número:
'''))
until = int(input(f'¿Hasta que valor quieres tu tabla?:'))

def run():
    for counter in range(1, until + 1):
        result = value * counter
        print(f' 😺 {value} x {counter} = {result}')


if __name__ == '__main__':
    run()
   
    
exit ("bye, bye, vuelve pronto")