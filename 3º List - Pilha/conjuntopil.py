from pilhasize import pilha

class conjuntopil:
    def __init__(self):
        self.fpil = None # Para armazenar as pilhas.
    
    def empty(self):
        return self.fpil is None

    def push(self,valor):
        if self.empty() or self.fpil.size >= self.fpil.maxsize: # Checa se esta vazio ou se ja chegou ao tamanho maximo.
            npil = pilha(self.fpil.maxsize)
            npil.push(valor)

            npil.prox = self.fpil
            self.fpil = npil
        else:
            self.fpil.push(valor)
    
    def pop(self):
        if self.empty():
            return print("Conjunto Vazio")
        aux = self.fpil.pop()

        if self.fpil.empty():
            self.fpil = self.fpil.prox
        
        return aux

    def peek(self):
        if self.empty():
            return print("Conjunto Vazio")
        val = self.fpil.peek()
        return val

    