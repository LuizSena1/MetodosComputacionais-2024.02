import time
from listmaker import listmaker
from Bubblesort import bubblesort
from Mergesort import mergesort

n = 10
origin = listmaker(n)
# Bubblesort
bublecopy = origin.copy()
vib = time.perf_counter()
orbuble = bubblesort(bublecopy)
vfb = time.perf_counter()
dif = vfb - vib

# Mergesort
mergecopy = origin.copy()
vim = time.perf_counter()
ormerge = mergesort(mergecopy)
vif = time.perf_counter()
difm = vif - vim

# Prints
print(f'\nVetor Original: {origin}\n')
print(f'Vetor Organizado por Bubble: {orbuble}\nTempo de Execução Bubble:{dif:.6f}\n')
print(f'Vetor Organizado por Merge: {ormerge}\nTempo de Execução Merge:{difm:.6f}\n')

