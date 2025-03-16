class pilhavetor:
    def __init__(self, N):
        self.N = N # Tamanho do Vetor
        self.vet = [None] * self.N
        self.top = None
    
    def empty(self):
        return self.top is None
    
    def push(self,valor):
        if self.empty() or self.top + 1 < self.N:
            if self.empty():
                self.top = 0 # Topo assume essa posição.
            else:
                self.top += 1 # Passa topo para a proxima casa do Vetor.
            self.vet[self.top] = valor
        else:
            return print("Pilha cheia, Não e possivel Adicionar mais nenhum elemento. Libere memoria para continuar.")
    
    def pop(self):
        if self.empty():
            return print("Pilha vazia, Parando processo...")
        aux = self.vet[self.top]
        self.vet[self.top] = None # Elimina o item no topo.
        if self.top == 0:
            self.top = None # Como não a mais elemento, so transforma em None
        else:
            self.top -= 1 # Desloca uma casa para traz.
        
        return aux

    def peek(self):
        if self.empty():
            return print("Fila Vazia, Encerrando Processo...")
        return self.vet[self.top]


