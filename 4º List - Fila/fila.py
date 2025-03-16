from Node import node
from Invert import pilha
class Fila:
    def __init__(self):
        self.begin = None # Inicio da Fila
        self.end = None # Fim da Fila
    
    def empty(self):
        return self.begin is None

    def push(self,valor):
        n_no = node(valor)
        if self.empty():
            self.begin = n_no
        else:
            self.end.prox = n_no # Define o proximo no do end atual para o n_no
        
        self.end = n_no # Por fim, atualiza o fim para o n_no.

    def pop(self):
        if self.empty():
            return print("Fila Vazia! Encerrando Processo")
        aux = self.begin
        self.begin = aux.prox
        if self.begin is None:
            self.end = None
        
        return aux.info

    def clean(self):
        self.begin = None
        self.end = None

    def display(self):
        if self.empty():
            return print("Fila Vazia! Nada a Imprimir, Encerrando Processo...")
        print("|Fila:",end=" ")
        aux = self.begin
        while aux != None:
            print(aux.info,end=" ")
            aux = aux.prox
        print("|")

    def rotate(self,n):
        if self.empty():
            return print("Lista Vazia! Encerrando Processo...")
        
        for _ in range(n):
            vr = self.pop() # vr = Valor Removido, Remove o Elemento.
            self.push(vr)
        
        print(f"Processo Concluido, Fila foi Rotacionada {n} Vezes\n Imprimindo Fila...")
        self.display()

    def inverte(self):
        aux = pilha()
        while not self.empty(): # Roda enquanto a Fila Tiver Valor.
            vr = self.pop() # Retira o Valor da Fila
            aux.push(vr) # E insere na pilha, como ambas trabalham invertido, Fila - First in first our, e Pilha - First in Last Out. Isso inverte a posição dos valores
        while not aux.empty(): 
            inv = aux.pop() # Aqui se faz o inverso, retira os itens da pilha
            self.push(inv) # E insere na fila, para se ter a Fila invertida.
        print("Fila invertida com Sucesso\n Imprimindo Fila...")
        self.display()
