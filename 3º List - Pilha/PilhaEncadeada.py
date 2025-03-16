from Node import node

class pilha():
    def __init__(self):
        self.top = None
    
    def empty(self):
        return self.top is None

    def push(self,valor): # Inserindo Elementos na Pilha. 
        n_no = node(valor)
        n_no.prox = self.top # Liga o novo no criado ao antigo Topo.
        self.top = n_no # Agora o novo topo, vira o novo nó
    
    def pop(self): # Remove o Elemento do Topo da pilha.
        if self.empty():
            return print("Pilha Vazia!")
        no = self.top
        self.top = self.top.prox
        return no.info

    def peek(self): # Mostra qual o elemento no Topo da Pilha.
        if self.empty():
            return print("Pilha Vazia!")
        return self.top.info
       