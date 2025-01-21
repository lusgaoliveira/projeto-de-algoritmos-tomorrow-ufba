from typing import List

Vector = List[int]

def soma_exata(vector: Vector, x: int) -> bool:

    tamanho = len(vector)
    for i in range(tamanho):
        num_atual = vector[i]

        for j in range(tamanho):
            if num_atual == vector[j]:
                pass
            else:
                soma = num_atual + vector[j]
                if soma == x:
                    return True
    return False


print(soma_exata([1, 2, 4, 4, 5], 8))  
