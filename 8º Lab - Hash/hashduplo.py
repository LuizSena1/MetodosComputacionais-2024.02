class HashTable:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
    
    def _hash1(self, key, tent):
        return hash(key) % self.capacity
    
    def _hash2(self, key, tent):
        return 1 + (hash(key) % (self.capacity - 1))

    def findslot(self,key,insr):
        index = self._hash1(key)
        aux = self._hash2(key)
        findex = None

        while True:
            if self.table[index] is None:
                if not insr:
                    return None, None
                return index if findex is None else findex,aux
            elif self.table[index][0] == key:
                return index, aux
            
            elif findex is None and self.table[index] is False:
                findex = index
            
            index = (index + aux) % self.capacity


    def insert(self,key,valor):
        if self.size / self.capacity >= 0.7:
            self.resize()
            
        index, aux = self.findslot(key,True)
        if index is not None:
            self.table[index] = (key,valor)
            self.size += 1

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
        index, aux = self.findslot(key,False)
        if index is None:
            return f"Chave {key} não encontrada"
        
        self.table[index] = None
        self.size -= 1
        nindex = (index + aux) % self.capacity
        while self.table[nindex] is not None:
            keha, vaeha = self.table[nindex]
            self.table[nindex] = None
            self.size -= 1
            self.insert(keha, vaeha)
            nindex = (nindex + aux) % self.capacity

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