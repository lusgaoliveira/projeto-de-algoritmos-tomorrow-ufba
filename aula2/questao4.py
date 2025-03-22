from typing import List

Vetor = List[int]

def ordena_por_selecao(vetor : Vetor) -> Vetor:
    controle = True
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            controle = False
            
    if not controle:
        for i in range(len(vetor)): # n
            menor = i # 1
            for j in range(i + 1, len(vetor)): # pa, mas vou considerar n
                if vetor[j] < vetor[menor]: # 1
                    menor = j # 1
            
            aux = vetor[i] # 1
            vetor[i] = vetor[menor] # 1
            vetor[menor] = aux # 1

        return vetor #1
# n + 1 + n + 1 + 1 + 1 + 1 + 1 = 2n + 6

print(ordena_por_selecao([3, 4, 1, 10]))
print(ordena_por_selecao([12, 10, 2, 5]))
print(ordena_por_selecao([12, 10, 2, 5]))
