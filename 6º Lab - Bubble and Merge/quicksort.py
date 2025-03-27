def quicksort(vetor):
    quicksortaux(vetor,0,len(vetor)-1)
    return vetor

def partiton(vetor,first,last):
    pivo = vetor[first]

    i = first - 1
    for j in range(first + 1,last + 1):
        if vetor[j] <= pivo:
            (vetor[i], vetor[j]) = (vetor[j],vetor[i])
            i += 1
    (vetor[i + 1], vetor[last]) = (vetor[last],vetor[i + 1])
    #(vetor[first], vetor[i - 1]) = (vetor[i - 1],vetor[first])
    return i + 1

def quicksortaux(vetor,first,last):
    if first < last:
        split = partiton(vetor, first, last)
        quicksortaux(vetor, first, split-1)
        quicksortaux(vetor, split+1, last)