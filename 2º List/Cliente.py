class cliente:
    def __init__(self,nome,senha):
        self.nome = nome
        self.senha = senha
        self.prox = None

class atendimento:
    def __init__(self):
        self.head = None
        self.word = 1

    def inserir(self, nome):
        n_client = cliente(nome,self.word)
        self.word += 1

        if self.vazio(): # Checando se a fila de atendimento esta Vazia.
            self.head = n_client
        else:
            aux = self.head
            while aux.prox: # Percorre ate o fim da Lista.
                aux = aux.prox
            aux.prox = n_client # Insere no fim da lista a informação.
        
        return n_client

    def atendido(self):
        if self.vazio():
            return print("Fila Vazia, não há ninguem a ser removido")
        
        aux = self.head
        self.head = self.head.prox # Como e para remover o primeiro termo, isso e suficiente.
    
    def imprimir(self):
        if self.vazio():
            return print("Ninguem a Listar. Não há clientes esperando atendimento")
    
        aux = self.head
        print("| Aguardando Atendimento |")
        while aux:
            print(f'| Nome: {aux.nome}, Senha: {aux.senha} |')
            aux = aux.prox # Passa para o Proximo Nó ate a lista acabar.

    def vazio(self):
        return self.head is None


