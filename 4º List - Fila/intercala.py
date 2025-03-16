from fila import Fila

def intercal(fila1,fila2):
    nfila = Fila()
    aux1 = fila1.begin
    aux2 = fila2.begin
    while aux1 or aux2:
        if aux1 != None:
            nfila.push(aux1.info)
            aux1 = aux1.prox
        if aux2 != None:
            nfila.push(aux2.info)
            aux2 = aux2.prox
    
    return nfila
