import time
import matplotlib.pyplot as plt
from listmaker import listmaker
from Bubblesort import bubblesort
from Mergesort import mergesort
from quicksort import quicksort
import numpy as np


n = [10, 100, 1000, 5000,10000]
bubletime = []
mergetime = []
quicktime = []

for i in range(len(n)):
        origin = listmaker(n[i])
        # Bubblesort
        bublecopy = origin.copy()
        vib = time.perf_counter()
        orbuble = bubblesort(bublecopy)
        vfb = time.perf_counter()
        dif = vfb - vib
        bubletime.append(dif)
        # Mergesort
        mergecopy = origin.copy()
        vim = time.perf_counter()
        ormerge = mergesort(mergecopy)
        vif = time.perf_counter()
        difm = vif - vim
        mergetime.append(difm)
        #Quicksort
        quickcopy = origin.copy()
        viq = time.perf_counter()
        orquick = quicksort(quickcopy)
        vfq = time.perf_counter()
        difq = vfq - viq
        quicktime.append(difq)

        print(f'\nN = {n[i]}')
        print(f'Tempo de Execução bubble:{dif:.6f}\nTempo de Execução Merge:{difm:.6f}\nTempo de Execução Quick:{difq:.6f}\n')

# plt.figure(figsize=(12,7))
# plt.plot(n,bubletime,label="Bubble Sort", marker = "o", linestyle="dotted", color="b")
# plt.plot(n,mergetime,label="Merge Sort",marker = "s", linestyle="dotted", color="r")
# plt.plot(n,quicktime,label="Quick Sort",marker="*",linestyle="dotted",color="purple")
# plt.xscale('log')
# plt.yscale('log')
# plt.xlabel("Tamanho do Vetor (n)")
# plt.ylabel("Tempo de Execução(em segundos) - Log")
# plt.title("Comparação de Velocidade de algoritimos")
# plt.xticks(n,labels=[str(val) for val in n])
# # Adiciona valores exatos
for x, y in zip(n, bubletime):
    plt.annotate(f'{y:.6f}', (x, y), textcoords="offset points", xytext=(0,5), ha='center', color="blue")
for x, y in zip(n, mergetime):
    plt.annotate(f'{y:.6f}', (x, y), textcoords="offset points", xytext=(0,5), ha='center', color="red")
for x, y in zip(n, quicktime):
    plt.annotate(f'{y:.6f}', (x, y), textcoords="offset points", xytext=(0,5), ha='center', color="purple")

# plt.legend()
# plt.grid(alpha = 0.5)
# plt.show()

plt.figure(figsize=(14, 8))
bar_width = 0.25
index = np.arange(len(n))
plt.xscale('log')
plt.yscale('log')
plt.bar(index, bubletime, bar_width, label='Bubble Sort', color='b')
plt.bar(index + bar_width, mergetime, bar_width, label='Merge Sort', color='r')
plt.bar(index + 2*bar_width, quicktime, bar_width, label='Quick Sort', color='purple')
for x, y in zip(n, bubletime):
    plt.annotate(f'{y:.6f}', (x, y), textcoords="offset points", xytext=(0,5), ha='center', color="blue")
for x, y in zip(n, mergetime):
    plt.annotate(f'{y:.6f}', (x, y), textcoords="offset points", xytext=(0,5), ha='center', color="red")
for x, y in zip(n, quicktime):
    plt.annotate(f'{y:.6f}', (x, y), textcoords="offset points", xytext=(0,5), ha='center', color="purple")

plt.xlabel('Tamanho do Vetor (n)')
plt.ylabel('Tempo Médio (s)')
plt.title('Comparação Direta de Tempos por Algoritmo')
plt.xticks(index + bar_width, n)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# plt.figure(figsize=(14, 8))
# bar_width = 0.25
# index = np.arange(len(n))

# # Cores personalizadas
# cores = ['#1f77b4', '#ff7f0e', '#9467bd']

# # Criação das barras
# barras1 = plt.bar(index - bar_width, bubletime, bar_width, label='Bubble Sort', color=cores[0])
# barras2 = plt.bar(index, mergetime, bar_width, label='Merge Sort', color=cores[1])
# barras3 = plt.bar(index + bar_width, quicktime, bar_width, label='Quick Sort', color=cores[2])

# # Configurações do gráfico
# plt.xlabel('Tamanho do Vetor (n)', fontsize=12)
# plt.ylabel('Tempo Médio de Execução (s)', fontsize=12)
# plt.title('Comparação de Desempenho entre Algoritmos de Ordenação', fontsize=14, pad=20)
# plt.xticks(index, n)
# plt.yscale('log')  # Mantém escala logarítmica para melhor visualização
# plt.grid(axis='y', alpha=0.3)

# # Função para adicionar valores nas barras
# def autolabel(barras, color):
#     for bar in barras:
#         height = bar.get_height()
#         plt.annotate(f'{height:.6f}',
#                      xy=(bar.get_x() + bar.get_width()/2, height),
#                      xytext=(0, 3),  # Deslocamento vertical
#                      textcoords="offset points",
#                      ha='center', va='bottom',
#                      color=color,
#                      fontsize=8)

# # Adiciona valores em todas as barras
# autolabel(barras1, cores[0])
# autolabel(barras2, cores[1])
# autolabel(barras3, cores[2])

# # Ajusta o espaçamento
# plt.margins(y=0.1)  # Espaço extra no topo para as anotações
# plt.legend(loc='upper left', fontsize=10)
# plt.tight_layout()

# # Linha de referência para melhoria na leitura
# for y in [0.001, 0.01, 0.1, 1, 10]:
#     plt.axhline(y=y, color='gray', linestyle='--', alpha=0.2, linewidth=0.5)

# plt.show()