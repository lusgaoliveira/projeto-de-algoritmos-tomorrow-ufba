from typing import List

sequencia = List[str]

def bem_formado(vetor: sequencia) -> bool:
    
    # Criei um dicionário para mapear abertura e fechamento
    pares = {'(' : ')', '[' : ']', '{' : '}'}
    pilha = ""

    for caracter in vetor:
        
        # Verifico se o caracter é de abertura, se sim adiciona na string
        if caracter in "([{":
            pilha += caracter

        # Verifico se é de fechamento, se sim, removo o último elemento da pilha que é de abertura e comparo
        elif caracter in ")]}":
            if not pilha:
                return False
            if pares[pilha[-1]] == caracter:
                # Faço um slice removendo o último elemento
                pilha = pilha[:-1]
            else:
                return False
    
    return pilha == ""
                

print(bem_formado(['{', '(', ')', '}']))
print(bem_formado(['{', '(', '(', '{', '}', ')', ')', '}']))
