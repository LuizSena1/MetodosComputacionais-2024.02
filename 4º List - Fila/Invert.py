from Node import node

class pilha:
    def __init__(self):
        self.top = None
    
    def empty(self):
        return self.top is None
    
    def push(self,val):
        n_no = node(val)
        n_no.prox = self.top
        self.top = n_no
    
    def pop(self): # Remove o Elemento do Topo da pilha.
        if self.empty():
            return print("Pilha Vazia! Encerrando Processo")
        no = self.top
        self.top = self.top.prox
        return no.info
    
    def peek(self):
        if self.empty():
            return print("Pilha Vazia")
        return self.top.info
