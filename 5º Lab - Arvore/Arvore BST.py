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
    
    def min(self):
        if self.vazio():
            return None

        aux = self
        while aux.esquerda is not None:
            aux = aux.esquerda
        
        return aux.info
    
    def max(self):
        if self.vazio():
            return None

        aux = self
        while aux.direita:
            aux = aux.direita
        
        return aux.info
    
    def bst(self,minv,maxv):
        
        if self.info <= minv or self.info >= maxv: # Se a raiz for menor que o minimo valor ou maior valor e invalido
            return False
        
        erdav = True
        direv = True
        if self.esquerda:
            erdav = self.esquerda.bst(minv,self.info)
        
        if self.direita:
            direv = self.direita.bst(self.info,maxv)

        return erdav and direv

    def validbst(self):
        if self.vazio():
            return True
        return self.bst(float('-inf'),float('inf'))

    def print_tree(self, level=0, prefix="Raiz: "):
        """Método auxiliar para visualizar a árvore"""
        print(" " * (level * 4) + prefix + str(self.info))
        if self.esquerda:
            self.esquerda.print_tree(level + 1, "L--> ")
        if self.direita:
            self.direita.print_tree(level + 1, "R--> ")

root = Arvore(None)
val = [50,30,70,20,40,60,80]
for i in range(len(val)):
    root.insertinfo(val[i])
    
root.print_tree()

if root.validbst:
    print("A arvore e uma BST Valida")
else:
    print("A Arvore nao e uma BST Valida")

print(f'Menor Valor da BST = {root.max()}')
print(f'Maior Valor da BST = {root.min()}')
