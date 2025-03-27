from queue import Queue
class Arvore():
    def __init__(self,info):
        self.info = info
        self.direita = None
        self.esquerda = None
    
    def vazio(self):
        return self.info == None

    def busca(self,valor):
        if self.vazio():
            return "Arvore Vazia"
        found = None
        if self.info == valor:
            found = self.info
            return found
        
        if self.esquerda:
            found = self.esquerda.busca(valor) # Roda a função na arvore esquerda ate o fim.
        if not found and self.direita:
            found = self.direita.busca(valor) # Roda a função na arvore direita ate o fim.
        
        return found
    
    def height(self):
        if self is None:
            return 0
        if self.esquerda:
            altesquerda = self.esquerda.height()
        else:
            altesquerda = 0
        if self.direita:    
            altdireita = self.direita.height()
        else:
            altdireita = 0
        return 1 + max(altdireita,altesquerda)

    def insert(self,valor):
        if self.vazio():
            return Arvore(valor)
        
        if valor < self.info:
            if self.esquerda:
                self.esquerda.insert(valor)
            else:
                self.esquerda = Arvore(valor)
        else:
            if self.direita:
                self.direita.insert(valor)
            else:
                self.direita = Arvore(valor)
        
        return self

    def full(self):
        if self.esquerda is None and self.direita is None:
            return True

        if self.esquerda and self.direita:
            return self.esquerda.full() and self.direita.full()

        return False
    
    def completa(self):
        q = Queue()
        q.put(self) # Adiciona a Raiz na fila pra ser usada.
        lacking = False
        while not q.empty():
            aux = q.get()

            if aux is None:
                lacking = True
                break
            else:
                if lacking:
                    return False
                if aux.esquerda:
                    q.put(aux.esquerda) 
                else:
                    q.put(None)
                if aux.direita:
                    q.put(aux.direita)
                else:
                    q.put(None)

        return True # Codigo correu inteiro sem problemas, significa que e completo.
    
    def cross(self):
        
        if self.esquerda and self.direita:
            return False
        
        if self.esquerda:
            esdegen = self.esquerda.cross()
        else:
            esdegen= True
        
        if self.direita:
            didegen = self.direita.cross()
        else:
            didegen = True
        
        return didegen and esdegen

    
    def definindo(self):
        
        cheia = self.full()
        degenerado = self.cross()
        complete = self.completa()

        if degenerado:
            return "A Arvore é Degenerada"
        
        if cheia and not complete:
            return "A Arvore é Cheia"
        elif cheia and complete:
            return "A Arvore é Cheia e Completa"
        else:
            return "A Arvore não se encaixa em nada"

    def pre_ordem(self):
        if self.vazio():
            return []
        elementos = [self.info]
        if self.esquerda:
            elementos += self.esquerda.pre_ordem()
        if self.direita:
            elementos += self.direita.pre_ordem()
        return elementos
    
    def em_ordem(self):
        if self.vazio():
            return []
        elementos = []
        if self.esquerda:
            elementos += self.esquerda.em_ordem()
        elementos.append(self.info)
        if self.direita:
            elementos += self.direita.em_ordem()
        return elementos
    
    def pos_ordem(self):
        if self.vazio():
            return []
        elementos = []
        if self.esquerda:
            elementos += self.esquerda.pos_ordem()
        if self.direita:
            elementos += self.direita.pos_ordem()
        elementos.append(self.info)
        return elementos
    def print_tree(self, level=0, prefix="Raiz: "):
        """Método auxiliar para visualizar a árvore"""
        print(" " * (level * 4) + prefix + str(self.info))
        if self.esquerda:
            self.esquerda.print_tree(level + 1, "L--> ")
        if self.direita:
            self.direita.print_tree(level + 1, "R--> ")


class __main__:
    root = Arvore(None)
    # b = Arvore('b')
    # c = Arvore('c')
    # d = Arvore('d')
    # e = Arvore('e')
    # f = Arvore('f')
    # a.esquerda = c
    # a.direita = b
    # c.esquerda = d
    # b.direita = e
    # e.direita = f
    root = root.insert('a')
    root.insert('b')
    root.insert('e')
    root.insert('o')
    root.insert('g')    
    root.insert('c')
    root.insert('d')
    root.insert('f')


    print(f'Em Ordem: {root.pre_ordem()}')
    print(f'Pos Ordem: {root.pos_ordem()}')
    print(f'Pre Ordem: {root.em_ordem()}')
    print(f"buscando por 'b': {root.busca('b')}")
    print(f'Altura de Arvore: {root.height()}')
    print(f'A Arvore e qual: {root.definindo()}')
    root.print_tree()