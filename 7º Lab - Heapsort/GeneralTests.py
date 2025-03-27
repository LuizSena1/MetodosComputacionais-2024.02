import time
from listmaker import listmaker
from Bubble import bubblesort
from merge import mergesort
from quicksort import quicksort
from Heap import Heap

n = [10, 100, 1000, 5000,10000]
bubletime = []
mergetime = []
quicktime = []
heaptime = []
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
        # Heapsort
        heapcopy = origin.copy()
        heap = Heap(len(heapcopy))
        for j in range(len(heapcopy)):
                heap.insert(heapcopy[j])
        vih = time.perf_counter()
        heap.heapsort()
        vfh = time.perf_counter()
        difh = vfh - vih
        heaptime.append(difh)

        print(f'N = {n[i]}')
        print(f'Tempo de Execução bubble:{dif:.6f}\nTempo de Execução Merge:{difm:.6f}\nTempo de Execução Quick:{difq:.6f}\nTempo de Execução Heap:{difh:.6f}')