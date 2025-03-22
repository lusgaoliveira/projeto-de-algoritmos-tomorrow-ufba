from typing import List
import time
import random
Vetor = List[int]

def insertion_sort(vetor : Vetor) -> Vetor: 
    for i in range(1, len(vetor)):
        j = i
        while j > 0 and vetor[j] < vetor[j - 1]:
            aux = vetor[j]
            vetor[j] = vetor[j - 1]
            vetor[j - 1] = aux
            j -= 1
    return vetor

lista = [random.randint(1, 100) for _ in range(30)]

tempo_inicial = time.time() 
lista_ordenada = insertion_sort(lista)
tempo_final = time.time()  

print("Lista ordenada: ", lista_ordenada)
print(f"Tempo de execução: {tempo_final - tempo_inicial:.5f} segundos")