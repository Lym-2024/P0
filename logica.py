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

def verificar_tokens(tokens:list)->bool:

    valido = True
    pos = 0
    instrucciones = []
    variables = []
    funciones = []

    return verificar_recursivo(valido,pos,instrucciones,tokens,variables,funciones)

def verificar_recursivo(valido:bool,pos:int,instrucciones:list,tokens:list,variables:list,funciones:list)->bool:

    if valido and len(tokens) > 0:
        if pos < len(tokens):
            token = tokens[pos]
            if token['tipo'] == 'lp':
                instrucciones.append('lp')
                pos += 1

                valido = verificar_recursivo(valido,pos,instrucciones,tokens,variables,funciones)
            
            elif token['tipo'] == 'rp':
                instrucciones.pop()
                pos += 1

                valido = verificar_recursivo(valido,pos,instrucciones,tokens,variables,funciones)
            
            elif token['value'] == 'defvar':
                name = tokens[pos+1]
                valor = tokens[pos+2]
                p = tokens[pos+3]

                if name['tipo'] == 'name' and (valor['tipo'] == 'constante' or valor['tipo'] == 'numero' or valor['value'] in variables) and p['tipo'] == 'rp':
                    variables.append(name['value'])
                    valido = verificar_recursivo(valido,pos+3,instrucciones,tokens,variables,funciones)
                else:
                    return False
            
            elif token['value'] == "=":
                name = tokens[pos +1]
                valor = tokens[pos+2]
                p = tokens[pos+3]

                if name['tipo'] == 'name' and (valor['tipo'] == 'constante' or valor['tipo'] == 'numero' or valor['value'] in variables) and (name['value'] in variables) and p['tipo'] == 'rp':
                    valido = verificar_recursivo(valido,pos+3,instrucciones,tokens,variables,funciones)
                else:
                    return False
                
            elif token['value'] == 'move':
                valor = tokens[pos+1]

                p = tokens[pos+2]

                if ((valor['tipo'] == 'name' and valor['value'] in variables) or valor['tipo'] == 'numero' or valor['tipo'] == 'constante') and p['tipo'] == 'rp':
                    valido = verificar_recursivo(valido,pos+2,instrucciones,tokens,variables,funciones)
                else:
                    return False
                
            elif token['value'] == 'skip':
                valor = tokens[pos+1]

                p = tokens[pos+2]
                
                if ((valor['tipo'] == 'name' and valor['value'] in variables) or valor['tipo'] == 'numero' or valor['tipo'] == 'constante') and p['tipo'] == 'rp':
                    valido = verificar_recursivo(valido,pos+2,instrucciones,tokens,variables,funciones)
                else:
                    return False
                
            elif token['value'] == 'turn':
                d = tokens[pos+1]

                p = tokens[pos+2]

                if d['tipo'] == 'constante' and (d['value'] == ':left' or d['value'] == ':right' or d['value'] == ':around') and p['tipo'] == 'rp':
                    valido = verificar_recursivo(valido,pos+2,instrucciones,tokens,variables,funciones)
                else:
                    return False
            
            elif token['value'] == 'face':
                d = tokens[pos+1]

                p = tokens[pos+2]

                if d['tipo'] == 'constante' and (d['value'] == ':north' or d['value'] == ':south' or d['value'] == ':west' or d['value'] == 'east') and p['tipo'] == 'rp':
                    valido = verificar_recursivo(valido,pos+2,instrucciones,tokens,variables,funciones)
                else:
                    return False
            
            elif token['value'] == 'put':
                d = tokens[pos+1]

                n = tokens[pos+2]

                p = tokens[pos+3]

                if d['tipo'] == 'constante' and (d['value'] == ':balloons' or d['value'] == ':chips') and (n['tipo']=='numero' or (n['tipo'] == 'name' and n['value'] in variables) or n['tipo'] == 'constante') and p['tipo'] == 'rp':
                    valido = verificar_recursivo(valido,pos+3,instrucciones,tokens,variables,funciones)
                else:
                    return False
            
            elif token['value'] == 'pick':
                d = tokens[pos+1]

                n = tokens[pos+2]

                p = tokens[pos+3]

                if d['tipo'] == 'constante' and (d['value'] == ':balloons' or d['value'] == ':chips') and (n['tipo']=='numero' or (n['tipo'] == 'name' and n['value'] in variables) or n['tipo'] == 'constante') and p['tipo'] == 'rp':
                    valido = verificar_recursivo(valido,pos+3,instrucciones,tokens,variables,funciones)
                else:
                    return False
                
            elif token['value'] == 'move-dir':
                n = tokens[pos+1]

                d=tokens[pos+2]

                p = tokens[pos+3]

                if d['tipo'] == 'constante' and (d['value'] == ':front' or d['value'] == ':back' or d['value'] == ':right' or d['value'] == ':left') and (n['tipo']=='numero' or (n['tipo'] == 'name' and n['value'] in variables) or n['tipo'] == 'constante') and p['tipo'] == 'rp':
                    valido = verificar_recursivo(valido,pos+3,instrucciones,tokens,variables,funciones)
                else:
                    return False
                
            elif token['value'] == 'run-dirs':
                pos = pos +1
                while tokens[pos]['tipo'] != 'rp' and pos < len(tokens):
                    d = tokens[pos]
                    if d['tipo'] == 'constante' and (d['value'] == ':front' or d['value'] == ':back' or d['value'] == ':right' or d['value'] == ':left'):
                        pos = pos+1
                    else:
                        valido = False
                if valido and pos < len(tokens):
                    valido = verificar_recursivo(valido,pos,instrucciones,tokens,variables,funciones)
            
            elif token['value'] == 'move-face':
                n = tokens[pos+1]

                d=tokens[pos+2]

                p = tokens[pos+3]

                if d['tipo'] == 'constante' and (d['value'] == ':north' or d['value'] == ':south' or d['value'] == ':west' or d['value'] == ':east') and (n['tipo']=='numero' or (n['tipo'] == 'name' and n['value'] in variables) or n['tipo'] == 'constante') and p['tipo'] == 'rp' :
                    valido = verificar_recursivo(valido,pos+3,instrucciones,tokens,variables,funciones)
                else:
                    return False
            
            elif token['value'] == 'null':
                p = tokens[pos+1]

                if p['tipo'] == 'rp':
                    valido = verificar_recursivo(valido,pos+1,instrucciones,tokens,variables,funciones)
                else:
                    return False

            elif token['value'] == 'if':
                cond = []
                pos =pos +1
                if tokens[pos+1]['value'] != 'not':
                    while tokens[pos]['tipo'] != 'rp' and pos < len(tokens):
                        cond.append(tokens[pos])
                        pos += 1
                    if pos < len(tokens):
                        cond.append(tokens[pos])
                        pos+=1
                else:
                    pos = pos +2
                    while tokens[pos]['tipo'] != 'rp' and pos < len(tokens):
                        cond.append(tokens[pos])
                        pos += 1
                    if pos < len(tokens):
                        cond.append(tokens[pos])
                        pos+=2
                
                b1 = []
                b1.append(tokens[pos])
                actual = len(instrucciones)+1
                instrucciones.append('lp')
                limite = len(instrucciones)-1
                pos = pos + 1
                while actual != limite and pos < len(tokens):
                    b1.append(tokens[pos])
                    if tokens[pos]['tipo'] == 'lp':
                        actual += 1
                        instrucciones.append('lp')
                    elif tokens[pos]['tipo'] == 'rp':
                        actual -= 1
                        instrucciones.pop()
                    pos += 1
                
                b2 = []
                b2.append(tokens[pos])
                actual = len(instrucciones)+1
                instrucciones.append('lp')
                limite = len(instrucciones)-1
                pos = pos + 1
                while actual != limite and pos < len(tokens):
                    b2.append(tokens[pos])
                    if tokens[pos]['tipo'] == 'lp':
                        actual += 1
                        instrucciones.append('lp')
                    elif tokens[pos]['tipo'] == 'rp':
                        actual -= 1
                        instrucciones.pop()
                    pos += 1
                
                if verificar_recursivo(True,0,[],b1,variables,funciones) and verificar_recursivo(True,0,[],b2,variables,funciones) and verificar_cond(cond,variables):
                    valido = verificar_recursivo(valido,pos,instrucciones,tokens,variables,funciones)
                else:
                    return False
            
            elif token['value'] == 'loop':
                cond = []
                pos =pos +1
                if tokens[pos]['value'] != 'not':
                    while tokens[pos]['tipo'] != 'rp' and pos < len(tokens):
                        cond.append(tokens[pos])
                        pos += 1
                    if pos < len(tokens):
                        cond.append(tokens[pos])
                        pos+=1
                else:
                    pos = pos + 2
                    while tokens[pos]['tipo'] != 'rp' and pos < len(tokens):
                        cond.append(tokens[pos])
                        pos += 1
                    if pos < len(tokens):
                        cond.append(tokens[pos])
                        pos+=2
                
                b2 = []
                actual = len(instrucciones)+1
                b2.append(tokens[pos])
                limite = len(instrucciones)
                instrucciones.append('lp')
                pos = pos + 1
                while actual != limite and pos < len(tokens):
                    b2.append(tokens[pos])
                    if tokens[pos]['tipo'] == 'lp':
                        actual += 1
                        instrucciones.append('lp')
                    elif tokens[pos]['tipo'] == 'rp':
                        actual -= 1
                        instrucciones.pop()
                    pos += 1
                b2.pop()

                if verificar_cond(cond,variables) and verificar_recursivo(True,0,[],b2,variables,[]):
                    valido = verificar_recursivo(valido,pos,instrucciones,tokens,variables,funciones)
                else:
                    return False
            
            elif token['value'] == 'repeat':
                n = tokens[pos +1]
                if n['tipo'] == 'numero' or (n['tipo']=='name' and n['value'] in variables) or n['tipo'] == 'constante':
                    pos = pos+2
                    b2 = []
                    actual = len(instrucciones)+1
                    b2.append(tokens[pos])
                    limite = len(instrucciones)
                    instrucciones.append('lp')
                    pos = pos + 1
                    while actual != limite and pos < len(tokens):
                        b2.append(tokens[pos])
                        if tokens[pos]['tipo'] == 'lp':
                            actual += 1
                            instrucciones.append('lp')
                        elif tokens[pos]['tipo'] == 'rp':
                            actual -= 1
                            instrucciones.pop()
                        pos += 1
                    
                    if verificar_recursivo(True,0,[],b2,variables,[]):
                        valido = verificar_recursivo(valido,pos,instrucciones,tokens,variables,funciones)
                    else:
                        return False
                else:
                    return False
            
            elif token['value'] == 'defun':
                n = tokens[pos+1]
                if n['tipo'] == 'name':
                    fun = {'name':n['value'],'par':0}
                    pos = pos+2
                    b1 = []
                    while tokens[pos]['tipo'] != 'rp' and pos < len(tokens):
                        b1.append(tokens[pos])
                        pos += 1
                    if pos < len(tokens):
                        b1.append(tokens[pos])
                        pos+=1

                    b2 = []
                    actual = len(instrucciones)+1
                    b2.append(tokens[pos])
                    limite = len(instrucciones)-1
                    instrucciones.append('lp')
                    pos = pos + 1
                    while actual != limite and pos < len(tokens):
                        b2.append(tokens[pos])
                        if tokens[pos]['tipo'] == 'lp':
                            actual += 1
                            instrucciones.append('lp')
                        elif tokens[pos]['tipo'] == 'rp':
                            actual -= 1
                            instrucciones.pop()
                        pos += 1
                    b2.pop()
                    if verificar_parametros(b1)[0]:
                        fun['par'] = verificar_parametros(b1)[1]
                        funciones.append(fun)
                        if verificar_recursivo(True,0,[],b2,verificar_parametros(b1)[2]+variables,funciones):
                            valido = verificar_recursivo(valido,pos,instrucciones,tokens,variables,funciones)
                    else:
                        return False
                else:
                    return False
            
            elif token['tipo'] == 'name':
                b1 = []
                pos = pos +1
                while tokens[pos]['tipo'] != 'rp' and pos < len(tokens):
                    b1.append(tokens[pos])
                    pos += 1
                
                fun_parcial = {'name':token['value'], 'par':len(b1)}

                if verificar_parametros2(b1,variables) and fun_parcial in funciones:
                    valido = verificar_recursivo(valido,pos,instrucciones,tokens,variables,funciones)
                else:
                    return False
            
            else:
                return False
        elif len(instrucciones) == 0:
            return True
        
        return valido
    else:
        return False
    
def verificar_cond(cond:list,variables:list)->bool:

    if cond[0]['tipo'] == 'lp' and cond[len(cond)-1]['tipo'] == 'rp':
        if (cond[1]['value'] == 'facing?' or cond[1]['value'] == 'can-move?') and len(cond) == 4:
            if cond[2]['tipo'] == 'constante' and (cond[2]['value'] == ':north' or cond[2]['value'] == ':south' or cond[2]['value'] == ':east' or cond[2]['value'] == ':west'):
                return True
            else:
                return False                  
        elif cond[1]['value'] == 'blocked?' and len(cond)==3:
            return True
        elif (cond[1]['value'] == 'can-put?' or cond[1]['value'] == 'can-pick?') and len(cond) == 5:
            if cond[2]['tipo'] == 'constante' and (cond[2]['value'] == ':balloons' or cond[2]['value'] == ':chips'):
                if cond[3]['tipo'] == 'constante' or cond[3]['tipo'] == 'numero' or (cond[3]['tipo'] == 'name' and cond[3]['value'] in variables):
                    return True
                else:
                    return False
            else:
                return False
        elif cond[1]['value'] == 'iszero?' and len(cond) == 4:
            if cond[2]['tipo'] == 'constante' or cond[2]['tipo'] == 'numero' or (cond[2]['tipo'] == 'name' and cond[2]['value'] in variables):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def verificar_parametros(parametros:list)->tuple:
    par = 0
    lista = []
    if parametros[0]['tipo'] == 'lp' and parametros[len(parametros)-1]['tipo'] == 'rp':
        for i in range(1,len(parametros)-1):
            if parametros[i]['tipo'] == 'name':
                par += 1
                lista.append(parametros[i]['value'])
            else:
                return (False,0,lista)
        return (True,par,lista)
    else:
        return (False,0,lista)
    
def verificar_parametros2(parametros:list,variables)->bool:
    for i in range(0,len(parametros)):
        if not((parametros[i]['tipo'] == 'name' and parametros[i]['value'] in variables) or parametros[i]['tipo'] == 'constante' or parametros[i]['tipo'] == 'numero'):
            return False
    return True