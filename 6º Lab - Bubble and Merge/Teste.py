import time
import matplotlib.pyplot as plt
from listmaker import listmaker
from Bubblesort import bubblesort
from Mergesort import mergesort
from quicksort import quicksort
import numpy as np

n = [10, 100, 1000, 5000, 10000]
bubletime = []
mergetime = []
quicktime = []
num = 1000  # Número de execuções por tamanho

for tamanho in n:
    tbubbles = []
    tmerge = []
    tquick = []
    
    for _ in range(num):
        vetor = listmaker(tamanho)  # Novo vetor a cada execução
        
        # Bubble Sort
        inicio = time.perf_counter()
        bubblesort(vetor.copy())
        fim = time.perf_counter()
        tbubbles.append(fim - inicio)
        
        # Merge Sort
        inicio = time.perf_counter()
        mergesort(vetor.copy())
        fim = time.perf_counter()
        tmerge.append(fim - inicio)
        
        # Quick Sort
        inicio = time.perf_counter()
        quicksort(vetor.copy())
        fim = time.perf_counter()
        tquick.append(fim - inicio)
    
    
    # Calcula a média
    bubletime.append(sum(tbubbles) / num)
    mergetime.append(sum(tmerge) / num)
    quicktime.append(sum(tquick) / num)


plt.figure(figsize=(14, 8))
index = np.arange(len(n))
plt.xscale('log')
plt.yscale('log')

plt.plot(n, bubletime, marker='o', linestyle='-', color='b', label='Bubble Sort')
plt.plot(n, mergetime, marker='s', linestyle='-', color='r', label='Merge Sort')
plt.plot(n, quicktime, marker='^', linestyle='-', color='purple', label='Quick Sort')

for x, y in zip(n, bubletime):
    plt.annotate(f'{y:.6f}', (x, y), textcoords="offset points", xytext=(0,5), ha='center', color="blue")
for x, y in zip(n, mergetime):
    plt.annotate(f'{y:.6f}', (x, y), textcoords="offset points", xytext=(0,5), ha='center', color="red")
for x, y in zip(n, quicktime):
    plt.annotate(f'{y:.6f}', (x, y), textcoords="offset points", xytext=(0,5), ha='center', color="purple")
plt.xlabel('Tamanho do Vetor (n)')
plt.ylabel('Tempo Médio (s)')
plt.title('Comparação de Eficiencia dos Algoritmo')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
