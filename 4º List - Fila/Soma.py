#from FilaTam import TFila as TFila
from fila import Fila

def soma(fila1,fila2):
    if fila1.size != fila2.size:
        return print("As filas não possuem o mesmo tamanho")
    nfila = Fila()
    aux1 = fila1.begin
    aux2 = fila2.begin

    while aux1:
        som = aux1.info + aux2.info
        nfila.push(som)
        aux1 = aux1.prox
        aux2 = aux2.prox
    
    return nfila
