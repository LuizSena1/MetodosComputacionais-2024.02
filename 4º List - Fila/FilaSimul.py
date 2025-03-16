from Invert import pilha
class simulation:
    def __init__(self):
        self.pilha1 = pilha()
        self.pilha2 = pilha()
    
    def enqueue(self, valor):
        self.pilha1.push(valor)
    
    def dequeue(self):
        if self.pilha1.empty():
            return print("Não a nada a remover")

        if self.pilha2.empty(): # Primeira checagem, para ver se pilha 2 esta vazia, e preenche-la
            while not self.pilha1.empty(): # enquanto pilha 1 tiver valor
                self.pilha2.push(self.pilha1.pop()) # o valor e posto na pilha 2
        
        if self.pilha2.empty(): # Checa se ainda esta vazia apos o codigo anterior
            return print("Fila Vazia")

        temp = self.pilha2.pop() # variavel temporaria para facilitar a vida
        while not self.pilha2.empty(): # Faz o inverso do codigo mais acima, enquanto tiver valor em pilha 2
            self.pilha1.push(self.pilha2.pop()) # Insere o valor na pilha 1. 
        
        return temp # Retorna o temp, que seria o topo da pilha 2 apos a inversão.
    
    def peek(self):
        if self.pilha1.empty():
            return print("Fila Vazia")
        
        if self.pilha2.empty():
            while not self.pilha1.empty():
                self.pilha2.push(self.pilha1.pop())

        temp = self.pilha2.peek()

        while not self.pilha2.empty():
            self.pilha1.push(self.pilha2.pop())
            
        return temp

    def display(self):
        if self.pilha1.empty():
            return print("Fila Vazia")
        
        if self.pilha2.empty():
            while not self.pilha1.empty():
                self.pilha2.push(self.pilha1.pop())
        print("|Fila:",end=" ")
        aux = self.pilha2.top
        while aux != None:
            print(aux.info,end=" ")
            aux = aux.prox
        print("|")

