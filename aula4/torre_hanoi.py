import time

def torre_de_hanoi(n, x, y, z):
    if n == 1:
        return
    torre_de_hanoi(n-1, x, z, y)
    torre_de_hanoi(n-1, z, y, x)

tempo_inicial = time.time()
torre_de_hanoi(30, "A", "B", "C")
tempo_final = time.time()
print(f"Tempo de execução: {tempo_final - tempo_inicial:.5f} segundos")
