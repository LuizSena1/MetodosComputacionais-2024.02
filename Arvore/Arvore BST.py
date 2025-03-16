class Arvore():
    def __init__(self,info):
        self.info = info
        self.direita = None
        self.esquerda = None
    
    def vazio(self):
        return self.info == None
    
    def insertpos(self,valor):
        if self.vazio() or valor is None:
            return

        if valor > self.info:
            if self.direita is None:
                self.direita = Arvore(valor) # Cria um novo no na arvore.
            else:
                self.direita.insertpos(valor) # Chama a função novamente ate não precisar mais
        else:
            if self.esquerda is None:
                self.esquerda = Arvore(valor) # Mesma coisa acima
            else:
                self.esquerda.insertpos(valor) # Novamente mesma coisa.
        
        return self


    def insertinfo(self,valor):
        if self.vazio():
            self.info = valor
        else:
            self.insertpos(valor)
    
    def deleta(self,valor):
        if valor > self.info:
            if self.direita():
                self.direita = self.deleta(self.direita,valor)
        elif valor < self.info:
            if self.esquerda():
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
        
        return self
    

root = Arvore(10)
root.insertinfo(11)
root.insertinfo(12)
root.insertinfo(13)
root.insertinfo(14)
root.insertinfo(15)
root.insertinfo(9)
root.insertinfo(8)
root.insertinfo(7)
root.insertinfo(6)
root.insertinfo(5)