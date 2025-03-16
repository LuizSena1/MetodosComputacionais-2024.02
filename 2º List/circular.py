class No:
    def __init__(self, info):
        self.info = info # Definindo o Valor do Nó.
        self.prox = None # Apontando para o Proximo Nó.

class ListaCircular:
    def __init__(self):
        self.head = None
    
    def vazio(self):
        return self.head is None
    
    def inserir(self, valor):
        n_no = No(valor)
        if self.vazio(): # Se Lista estiver vazia.
            self.head = n_no # Cria um Novo Nó para a lista
            n_no.prox = self.head # Como a lista e pra ser circular, O Novo Nó criado, aponta pra si mesmo.

        else: # Normal, quando a lista ja possuir algum item inserido
            aux = self.head # Sera usado para auxiliar e percorrer a lista "toda" ate chegar no ultimo no. Onde seria o self.head.
            while aux.prox != self.head: # Como dito, percorre enquanto o aux.prox não for igual ao self.head
                aux = aux.prox
            aux.prox = n_no
            n_no.prox = self.head


    def imprimir(self):

        if self.vazio(): # Como de costume, checa se a lista esta Vazia, se tiver. Vai dar o print
            return print("\nLista esta Vazia.")

        aux = self.head
        print("\n| Imprimindo Lista:",end=" ")
        while aux:
            print(aux.info , end=" ")
            aux = aux.prox

            if aux == self.head:
                break
        print("|")

    def remover(self,valor):
        if self.vazio():
            return print("Lista Vazia")
        ant = self.head
        p = self.head.prox

        while(p.info != valor and p != self.head):
            ant = p
            p = p.prox
        
        if p.info == valor: # Diferente de lista normal, essa não vai ficar None quando o loop for concluido
            
            if p.prox == p: # Isso fara a lista ficar vazia, no caso de o item a ser removido for o unico na lista.
                self.head = None
                return self.head
            
            if p == self.head: # Caso o Item seja o primeiro da lista.
                self.head = p.prox # Faz com que o primeiro valor seja eliminado, e segundo valor se torne o primeiro da lista.
            else:
                ant.prox = p.prox
                p = None

        return self.head

    def limpar(self):
        if self.vazio(): # Primero checa se algo alguma ação e nescessaria.
            return None
        
        p = self.head.prox
        while p != self.head: # Percorre a lista inteira ate fazer um Loop completo.
            aux = p # Define o auxiliar para p.info para ser utilizado e o loop continuar.
            p = p.prox # Define o P para seu proximo valor, pulando para o proximo nó
            aux.prox = None # Apaga a conexão com o proximo no 

        self.head.prox = None # Apaga a conexão com o proximo no
        self.head = None # Apaga o Nó em si e faz a lista ficar Vazia.
        
        return self.head

    def enderecos(self):

        if self.vazio(): # Como de costume, checa se a lista esta Vazia, se tiver. Vai dar o print
            return print("\nLista esta Vazia.")

        aux = self.head
        print("\n Imprimindo Lista Circular e endereços de memoria:")
        while aux:
            print(f"Elementos: {aux.info}, Endereços da Memoria:{id(aux.info)}")
            aux = aux.prox

            if aux == self.head:
                break
        print("")
    
    def duplicados(self):
        if self.vazio():
            return print("Lista Vazia.")
        
        p = self.head # Ponteiro inicial. Para definir o Nó atual.

        while True:
            aux = p # Auxiliar usado para verificar duplicados.

            while aux.prox != self.head: # Percore todo a lista ate chegar no "ultimo" Nó, que estaria apontando para o self.head
                
                if aux.prox.info == p.info: # Checa se o há algum valor duplicado, e se encontrar
                    aux.prox = aux.prox.prox # Ele remove o nó duplicado
                else:
                    aux = aux.prox # Caso não, apenas avança para o proximo nó.
            
            
            if p.prox == self.head: # Checa se o Loop foi concluido.
                break # E acaba o Loop.
        
            p = p.prox
