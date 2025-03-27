class Arvore():
    def __init__(self,info):
        self.info = info
        self.direita = None
        self.esquerda = None
        self.altura = 1

    def vazio(self):
        return self.info == None

    def height(self):
        if self.vazio():
            return 0
        else:
            return self.altura
        
    def hupdate(self):
        if self.esquerda:
            alt_esq = self.esquerda.altura
        else:
            alt_esq = 0
        
        if self.direita:
            alt_dir = self.direita.altura
        else:
            alt_dir = 0
        self.altura = 1 + max(alt_esq,alt_dir)

    def fbalance(self):
        if self.vazio():
            return 0
        else:
            if self.esquerda:
                alt_esq = self.esquerda.height()
            else:
                alt_esq = 0
            if self.direita:
                alt_dir = self.direita.height()
            else:
                alt_dir = 0
        return alt_esq - alt_dir

    def insert(self,valor):
        if self.vazio():
            self.info = valor
            self.altura = 1
        else:
            self.insertdata(valor)

    def insertdata(self,valor):
        if valor > self.info:
            if self.direita is None:
                self.direita = Arvore(valor)
            else:
                self.direita.insertdata(valor)
        else:
            if self.esquerda is None:
                self.esquerda = Arvore(valor)
            else:
                self.esquerda.insertdata(valor)
        
        return self.balancear()
        
    def rotation_direita(self):
        if not self.esquerda:
            return self

        aux = self.esquerda
        self.esquerda = aux.direita
        aux.direita = self
        self.hupdate()
        aux.hupdate()
        return aux

    def rotation_esquerda(self):
        if not self.direita:
            return self
        aux = self.direita
        self.direita = aux.esquerda
        aux.esquerda = self
        self.hupdate()
        aux.hupdate()
        return aux
    
    def balancear(self):
        fat = self.fbalance()

        if fat > 1: # Esquerda mais pesada
            if self.esquerda and self.esquerda.fbalance() <= 0:
                return self.rotation_direita()
            elif self.esquerda:
                self.esquerda = self.esquerda.rotation_esquerda()
                return self.rotation_direita()
        
        elif fat < -1: # Direita mais pesada
            if self.direita and self.direita.fbalance() > 0:
                return self.rotation_esquerda()
            elif self.direita:
                self.direita = self.direita.rotation_direita()
                return self.rotation_esquerda()
            
        return self
    
    def deleta(self,valor):

        if valor > self.info:
            if self.direita:
             self.direita = self.direita.deleta(valor)

        elif valor < self.info:
            if self.esquerda:
                self.esquerda = self.esquerda.deleta(valor)

        else:
            # Caso 1 - Folha
            if self.esquerda is None and self.direita is None:
                return None
            # Caso no qual apenas um filho(ou so esquerda ou so direita)
            elif self.esquerda is None:
                return self.direita
            elif self.direita is None:
                return self.esquerda
            
            else:
                aux = self.direita
                while aux.esquerda is not None:
                    aux = aux.esquerda
                self.info = aux.info
                self.direita = self.direita.deleta(aux.info)
        self.hupdate()
        return self.balancear()
    
    def numbernos(self):
        if self.vazio():
            return 0
        aux = 1
        if self.esquerda is not None:
            aux += self.esquerda.numbernos()
        if self.direita is not None:
            aux += self.direita.numbernos()
        
        return aux

    def print_tree(self, level=0, prefix="Raiz: "):
        """Método auxiliar para visualizar a árvore"""
        print(" " * (level * 4) + prefix + str(self.info))
        if self.esquerda:
            self.esquerda.print_tree(level + 1, "L--> ")
        if self.direita:
            self.direita.print_tree(level + 1, "R--> ")

# Criando a árvore
raiz = Arvore(30)
raiz.insert(20)
raiz.insert(40)
raiz.insert(10)
raiz.insert(25)
raiz.insert(35)
raiz.insert(50)
raiz.insert(5)
raiz.insert(15)

# Exibindo a árvore formatada
print("Árvore AVL:")
raiz.print_tree()

# Testando remoção
print("\nRemovendo 10...")
raiz = raiz.deleta(10)
raiz.print_tree()

print("\nRemovendo 30...")
raiz = raiz.deleta(30)
raiz.print_tree()

print(f'Tamanho da arvore: {raiz.numbernos()}')