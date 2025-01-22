from typing import List

sequencia = List[str]

def bem_formado(vetor: sequencia) -> bool:
    
    pares = {'(' : ')', '[' : ']', '{' : '}'}
    pilha = ""

    for caracter in vetor:
       
        if caracter in "([{":
            pilha += caracter

        elif caracter in ")]}":
            if not pilha:
                return False
            if pares[pilha[-1]] == caracter:
                pilha = pilha[:-1]
            else:
                return False
    
    return True if not pilha else False
                

print(bem_formado(['{', '(', ')', '}']))
print(bem_formado(['{', '(', '(', '{', '}', ')', ')', '}']))
