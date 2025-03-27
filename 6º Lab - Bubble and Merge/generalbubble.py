from listmaker import listmaker
from Bubblesort import bubblesort
n = 10
origin = listmaker(n)
# Bubblesort
print(f'\nVetor Original: {origin}')
bublecopy = origin.copy()
orbuble = bubblesort(bublecopy)
print(f'Vetor Organizado por Bubble: {orbuble}\n')