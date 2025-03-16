from Node import node
class TFila:
    def __init__(self,tam):
        self.begin = None
        self.end = None
        self.N = tam
        self.size = 0

    def empty(self):
        return self.begin is None
    
    def full(self):
        return self.N == self.size
    
    def push(self,val):
        if self.full():
            return print("Fila Cheia! Não e possivel adicionar elementos, Encerrando Processo...")

        n_no = node(val)

        if self.empty():
            self.begin = n_no
        else:
            self.end.prox = n_no
        
        self.end = n_no
        self.size += 1
    
    def pop(self):
        if self.empty():
            return print("Fila Vazia! Encerrando Processo")
        aux = self.begin
        self.begin = aux.prox
        if self.begin is None:
            self.end = None
        
        self.size -= 1
        return aux.info

    def clean(self):
        self.begin = None
        self.end = None
        self.size = 0
    
    def display(self):
        if self.empty():
            return print("Fila Vazia! Nada a Imprimir, Encerrando Processo...")
        print("|Fila:",end=" ")
        aux = self.begin
        while aux != None:
            print(aux.info,end=" ")
            aux = aux.prox
        print("|")

