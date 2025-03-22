from typing import List
import random

Vetor = List[int]

def particiona(lista: Vetor, esquerda: int, direita : int) -> int:
    pivo = lista[direita]
    i = esquerda - 1

    for j in range(esquerda, direita):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    lista[i + 1], lista[direita] = lista[direita], lista[i + 1]

    return i + 1


def quicksort(lista: Vetor, esquerda: int, direita: int) -> None:
    if esquerda < direita:
        q = particiona(lista, esquerda, direita)
        quicksort(lista, esquerda, q - 1)
        quicksort(lista, q+1, direita)


lista = [random.randint(1, 100) for _ in range(20)]
quicksort(lista, 0, len(lista) - 1)

print("Lista ordenada:", lista)