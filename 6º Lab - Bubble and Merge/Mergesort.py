def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    M = len(arr) // 2
    L = arr[:M] # Divide os elementos do inicio ate a casa anterior ao M
    R = arr[M:] # Divide os elementos do mid ate o final
    # Elementos recursivos para ordenar ambass as metades obitidas anteriormente.
    SL = mergesort(L) 
    SR = mergesort(R)

    # Chama a função merge no return, para que o mergesorte retorne o vetor ordenado.
    return merge(SL,SR)

def merge(esq, dir):
    resul = [] # Lista vazia a ser usada
    # Definido ponteiros a ser usados depois para percorer divisões.
    i = 0
    j = 0
    # Percorre enquanto o valor de i e j não serem iguais ao len dos vetores.
    while i < len(esq) and j < len(dir):
        # Compara o valor dos vetores e adiciona o menor valor a lista resul
        if esq[i] < dir[j]: 
            resul.append(esq[i])
            i += 1
        else:
            resul.append(dir[j])
            j += 1

    resul.extend(esq[i:])
    resul.extend(dir[j:])
    return resul