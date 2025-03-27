from Heap import Heap
import random

heap = Heap(10)
n = [2,3,1,4,6,5,9,7,8,10]
# for _ in range(10):
#     n.append(random.randrange(0,99))

for i in range(len(n)):
    heap.insert(n[i])
heap.definindo()
print("Heap elements:")
heap.imprime()
heap.heapsort()
print("Sorted Array:")
heap.imprime()