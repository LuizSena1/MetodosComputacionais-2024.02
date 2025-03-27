class HashTable:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
    
    def _hash(self, key, tent):
        a,b = 3,1
        return (hash(key)+ a*tent**2 + b*tent) % self.capacity

    def insert(self,key,valor):
        if self.size / self.capacity >= 0.7:
            self.resize()
            
        tentativa = 0
        index = self._hash()
        while self.table[index] is not None and self.table[index][0] != key:
            tentativa += 1
            index = self._hash(key,tentativa)
        
        if self.table[index] is None:
            self.size += 1
        self.table[index] = (key,valor)

    def busca(self,key):
        tent = 0
        index = self._hash(key,tent)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            tent += 1
            index = self._hash(key,tent)
        
        return None
    
    def deleta(self,key):
        tent = 0
        index = self._hash(key,tent)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self.size -= 1
                self.rehash(index)
                return
            tent += 1
            index = self._hash(key,tent)

        return None

    def _rehash(self, begin):
        index = (begin + 1) % self.capacity
        while self.table[index] is not None:
            key, valor = self.table[index]
            self.size -= 1
            self.insert(key, valor)
            index = (index + 1) % self.capacity 

    def resize(self):
        antigat = self.table
        ancietcap = self.capacity
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0 # reseta tudo
        for index in range(ancietcap):
            if antigat[index] is not None:
                self.insert(*antigat[index])