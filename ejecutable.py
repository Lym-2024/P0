import Intento as it

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

    return tokens

i = main1('ensayo.txt')
print('terminamos')