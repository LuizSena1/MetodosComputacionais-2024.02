from Node import node

class pilha:
    def __init__(self,maxsize = 10):
        self.top = None
        self.maxsize = maxsize
        self.size = 0
    
    def empty(self):
        return self.top is None

    def push(self,valor):
        if self.size >= self.maxsize:
            return print("A pilha atingiu o tamanho máximo")
        n_no = node(valor)
        n_no.prox = self.top
        self.top = n_no
        self.size += 1 # Aumenta o tamanho
    
    def pop(self):
        if self.empty():
            return print("Pilha Vazia")
        no = self.top
        self.top = self.top.prox
        self.size -= 1 # Diminui tamanho
        return no.info
    
    def peek(self): # Mostra qual o elemento no Topo da Pilha.
        if self.empty():
            return print("Pilha Vazia!")
        return self.top.info
