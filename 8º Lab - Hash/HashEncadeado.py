class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self,key,value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key,value)
            self.size += 1
        else:
            atual = self.table[index]
            while atual:
                if atual.key == key:
                    atual.value = value
                    return
                atual = atual.next
            nnode = Node(key,value)
            nnode.next = self.table[index]
            self.table[index] = nnode
            self.size += 1
    
    def busca(self, key):
        index = self._hash(key)

        atual = self.table[index]
        while atual:
            if atual.key == key:
                return atual.value
            atual = atual.next
        return None

    def remove(self, key):
        index = self._hash(key)

        ant = None
        atual = self.table[index]

        while atual:
            if atual.key == key:
                if ant:
                    ant.next = atual.next
                else:
                    self.table[index] = atual.next
                self.size -= 1
                return
            ant =  atual
            atual = atual.next
    
    def __str__(self):
        element = []
        for i in range(self.capacity):
            atual = self.table[i]
            while atual:
                element.append((atual.key,atual.value))
                atual  = atual.next
        return str(element)

    def __contains__(self,key):
        try:
            self.busca(key)
            return True
        except KeyError:
            return  False