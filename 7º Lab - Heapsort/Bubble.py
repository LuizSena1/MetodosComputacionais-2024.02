def bubblesort(vetor):
    tam = len(vetor)
    for i in range(tam):
        for j in range(0,tam-i-1):
            if vetor[j] > vetor[j+1]:
                vetor[j],vetor[j+1] = vetor[j+1],vetor[j]
    return vetor