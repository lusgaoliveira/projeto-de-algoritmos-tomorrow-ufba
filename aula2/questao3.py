from typing import List

Vetor = List[int]

def soma(vetor : Vetor) -> int:
    soma = 0 # 1
    for i in range(len(vetor)): # n 
        soma += vetor[i] # 2
    return soma # 1

print(soma([2, 5, 8]))
