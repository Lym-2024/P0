#Ejecutable (este es el archivo que se debe ejecutar)
import logica as it

def main1 (file_name:str)->bool:

    archivo = open(file_name)
    
    cadena = ''

    line = archivo.readline()
    while (line != ''):
        cadena += line.rstrip().strip().lower()
        line = archivo.readline()
    
    if len(cadena) == 0:
        return False

    tokens = it.generar_tokens(cadena)

    return it.verificar_tokens(tokens)

def main():
    print('Bienvenido.\n')
    file = input("Por favor, ingrese el nombre del archivo que contiene el programa (debe estar en la misma carpeta de este programa): ")
    r = main1(file)
    if r:
        print('Yes - la sintáxis del programa es correcta.')
    else:
        print('No - la sintáxis del programa no es correcta.')

main()