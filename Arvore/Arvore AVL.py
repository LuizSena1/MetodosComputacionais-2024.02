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
            return self.esquerda.height() - self.direita.height()

    def insertinfo(self,valor):
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
        aux = self.esquerda
        self.esquerda = aux.direita
        aux.direita = self
        self.hupdate()
        aux.hupdate()
        return aux

    def rotation_esquerda(self):
        aux = self.direita
        self.esquerda = aux.esquerda
        aux.esquerda = self
        self.hupdate()
        aux.hupdate()
        return aux
    
    def balancear(self):
        fat = self.fbalance()

        if fat > 1: # Esquerda mais pesada
            if self.esquerda.fbalance() <= 0:
                return self.rotation_direita()
            else:
                self.esquerda = self.esquerda.rotation_esquerda()
                return self.rotation_direita()
        
        elif fat < -1: # Direita mais pesada
            if self.direita.fbalance() >= 0:
                return self.rotation_esquerda
            else:
                self.direita = self.direita.rotation_direita()
                return self.rotation_esquerda
            
        return self
    
    def deleta(self,valor):

        if valor > self.info:
            if self.direita:
             self.direita = self.deleta(self.direita,valor)

        elif valor < self.info:
            if self.esquerda:
                self.esquerda = self.deleta(self.esquerda,valor)

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
                self.direita = self.deleta(self.direita,aux.info)
        self.hupdate()
        return self.balancear()