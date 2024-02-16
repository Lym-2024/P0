#Ensayo

def main1 (file_name:str)->bool:

    archivo = open(file_name)
    
    cadena = ''

    line = archivo.readline()
    while (line != ''):
        cadena += line.rstrip().strip().lower()
        line = archivo.readline()
    
    if len(cadena) == 0:
        return False

    tokens = generar_tokens(cadena)

    return tokens

def generar_tokens(cadena:str)->list:

    tokens = []

    pos = 0

    while (pos<len(cadena)):

        if cadena[pos] == ' ':
            pos += 1

        elif cadena[pos] == '(':
            token = {'tipo':'lp','value':'('}
            tokens.append(token)
            pos += 1
        
        elif cadena[pos] == ')':
            token = {'tipo':'rp','value':')'}
            tokens.append(token)
            pos += 1
        
        elif cadena[pos] == '=':
            token = {'tipo':'command','value':'='}
            tokens.append(token)
            pos += 1

        elif cadena[pos] == 'd':
            v1 = verificar(cadena,pos,'defvar')
            v2 = verificar(cadena,pos,'defun')
            if v1[0]:
                token = {'tipo':v1[3],'value':v1[2]}
                tokens.append(token)
                pos = v1[1]
            elif v2[0]:
                token = {'tipo':v2[3],'value':v2[2]}
                tokens.append(token)
                pos = v2[1]
            else:
                token = {'tipo':v1[3],'value':v1[2]}
                tokens.append(token)
                pos = v1[1]
        
        elif cadena[pos] == 'm':
            v1 = verificar(cadena,pos,'move')
            v2 = verificar(cadena,pos,'move-dir')
            v3 = verificar(cadena,pos,'move-face')
            if v1[0]:
                token = {'tipo':v1[3],'value':v1[2]}
                tokens.append(token)
                pos = v1[1]
            elif v2[0]:
                token = {'tipo':v2[3],'value':v2[2]}
                tokens.append(token)
                pos = v2[1]
            elif v3[0]:
                token = {'tipo':v3[3],'value':v3[2]}
                tokens.append(token)
                pos = v3[1]
            else:
                token = {'tipo':v3[3],'value':v3[2]}
                tokens.append(token)
                pos = v3[1]
        
        elif cadena[pos] == 's':
            v = verificar(cadena,pos,'skip')
            if v[0]:
                token = {'tipo':v[3],'value':v[2]}
                tokens.append(token)
                pos = v[1]
            else:
                token = {'tipo':v[3],'value':v[2]}
                tokens.append(token)
                pos = v[1]

        elif cadena[pos] == 't':
            v = verificar(cadena,pos,'turn')
            if v[0]:
                token = {'tipo':v[3],'value':v[2]}
                tokens.append(token)
                pos = v[1]
            else:
                token = {'tipo':v[3],'value':v[2]}
                tokens.append(token)
                pos = v[1]

        elif cadena[pos] == 'f':
            v1 = verificar(cadena,pos,'face')
            v2 = verificar(cadena,pos,'facing?')
            if v1[0]:
                token = {'tipo':v1[3],'value':v1[2]}
                tokens.append(token)
                pos = v1[1]
            elif v2[0]:
                token = {'tipo':v2[3],'value':v2[2]}
                tokens.append(token)
                pos = v2[1]
            else:
                token = {'tipo':v1[3],'value':v1[2]}
                tokens.append(token)
                pos = v1[1]
        
        elif cadena[pos] == 'p':
            v1 = verificar(cadena,pos,'put')
            v2 = verificar(cadena,pos,'pick')
            if v1[0]:
                token = {'tipo':v1[3],'value':v1[2]}
                tokens.append(token)
                pos = v1[1]
            elif v2[0]:
                token = {'tipo':v2[3],'value':v2[2]}
                tokens.append(token)
                pos = v2[1]
            else:
                token = {'tipo':v1[3],'value':v1[2]}
                tokens.append(token)
                pos = v1[1]

        elif cadena[pos] == 'r':
            v1 = verificar(cadena,pos,'run-dirs')
            v2 = verificar(cadena,pos,'repeat')
            if v1[0]:
                token = {'tipo':v1[3],'value':v1[2]}
                tokens.append(token)
                pos = v1[1]
            elif v2[0]:
                token = {'tipo':v2[3],'value':v2[2]}
                tokens.append(token)
                pos = v2[1]
            else:
                token = {'tipo':v1[3],'value':v1[2]}
                tokens.append(token)
                pos = v1[1]

        elif cadena[pos] == 'n':
            v1 = verificar(cadena,pos,'null')
            v2 = verificar(cadena,pos,'not')
            if v1[0]:
                token = {'tipo':v1[3],'value':v1[2]}
                tokens.append(token)
                pos = v1[1]
            elif v2[0]:
                token = {'tipo':v2[3],'value':v2[2]}
                tokens.append(token)
                pos = v2[1]
            else:
                token = {'tipo':v1[3],'value':v1[2]}
                tokens.append(token)
                pos = v1[1]
        
        elif cadena[pos] == 'i':
            v1 = verificar(cadena,pos,'if')
            v2 = verificar(cadena,pos,'iszero?')
            if v1[0]:
                token = {'tipo':v1[3],'value':v1[2]}
                tokens.append(token)
                pos = v1[1]
            elif v2[0]:
                token = {'tipo':v2[3],'value':v2[2]}
                tokens.append(token)
                pos = v2[1]
            else:
                token = {'tipo':v1[3],'value':v1[2]}
                tokens.append(token)
                pos = v1[1]
        
        elif cadena[pos] == 'l':
            v = verificar(cadena,pos,'loop')
            if v[0]:
                token = {'tipo':v[3],'value':v[2]}
                tokens.append(token)
                pos = v[1]
            else:
                token = {'tipo':v[3],'value':v[2]}
                tokens.append(token)
                pos = v[1]
        
        elif cadena[pos] == 'b':
            v = verificar(cadena,pos,'blocked?')
            if v[0]:
                token = {'tipo':v[3],'value':v[2]}
                tokens.append(token)
                pos = v[1]
            else:
                token = {'tipo':v[3],'value':v[2]}
                tokens.append(token)
                pos = v[1]
        
        elif cadena[pos] == 'c':
            v1 = verificar(cadena,pos,'can-put?')
            v2 = verificar(cadena,pos,'can-pick?')
            v3 = verificar(cadena,pos,'can-move?')
            if v1[0]:
                token = {'tipo':v1[3],'value':v1[2]}
                tokens.append(token)
                pos = v1[1]
            elif v2[0]:
                token = {'tipo':v2[3],'value':v2[2]}
                tokens.append(token)
                pos = v2[1]
            elif v3[0]:
                token = {'tipo':v3[3],'value':v3[2]}
                tokens.append(token)
                pos = v3[1]
            else:
                token = {'tipo':v3[3],'value':v3[2]}
                tokens.append(token)
                pos = v3[1]
        
        else:
            v = verificar(cadena,pos,'')
            token = {'tipo':v[3],'value':v[2]}
            tokens.append(token)
            pos = v[1]        
    
    return tokens

def verificar(cadena:str,pos:int,txt:str)->tuple:

    constantes = ['dim','myxpos','myypos','mychips','myballoons','balloonshere','chipshere','spaces',':left',':right',':around',':north',':south',':east',':west',':front',':back',':chips',':balloons']

    prueba = ''

    while (pos<len(cadena) and cadena[pos] != ' ' and cadena[pos] != '(' and cadena[pos] != ')'):
        prueba += cadena[pos]
        pos += 1
    
    if prueba == txt:
        return (True,pos,prueba,'command')
    
    elif prueba in constantes:
        return (False,pos,prueba,'constante')

    elif numeros(prueba):
        return (False,pos,prueba,'numero')

    else:
        return (False,pos,prueba,'name')
    
def numeros(cadena:str) -> bool:
    n = ['0','1','2','3','4','5','6','7','8','9']
    pos = 0

    num = True

    while(pos<len(cadena) and num):
        if cadena[pos] not in n:
            num = False
        else:
            pos += 1

    return num

    