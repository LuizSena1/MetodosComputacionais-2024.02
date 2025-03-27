class Heap:
    def __init__(self,size,type="max"):
        self.size = size
        self.vetor = []
        self.tamanhoheap = 0
        self.type = type

    def full(self):
        return self.tamanhoheap == self.size

    def vazio(self):
        return self.tamanhoheap == 0

    def definindo(self, val = None):
        if val == None:
            while True:
                val = int(input("Digite 1 para max heap, digite 2 para min heap: "))
                if val == 1:
                    self.type = "max"
                    break
                elif val == 2:
                    self.type = "min"
                    break
                else:
                    print("Digite 1 ou 2")
        elif val == 1:
            self.type = "max"
        else:
            self.type = "min"
            

    def esquerda(self,index):
        return 2 * index + 1
    
    def direita(self,index):
        return 2 * index + 2

    def parent(self,index):
        return (index-1) // 2
    
    def at(self,indicie):
        return self.vetor[indicie]
    
    def Heapfy(self, index, tamanho=None):
        if tamanho is None:
            tamanho = self.tamanhoheap
        left = self.esquerda(index)
        right = self.direita(index)
        aux = index
        if self.type == max:
            if left < tamanho and self.at(left) > self.at(aux):
                aux = left
            
            if right < tamanho and self.at(right) > self.at(aux):
                aux = right
        else:
            if left < tamanho and self.at(left) < self.at(aux):
                aux = left
            
            if right < tamanho and self.at(right) < self.at(aux):
                aux = right

            
        if aux != index:
            (self.vetor[index],self.vetor[aux]) = (self.vetor[aux],self.vetor[index])
            self.Heapfy(aux,tamanho)
        
        # aux = self.at(maior)
        # self.vetor[maior-1] = self.at(index)
        # self.vetor[index - 1] = aux
        # self.maxHeapfy(maior)

    def build_maxheap(self):
        self.tamanhoheap = len(self.vetor)
        n = self.tamanhoheap // 2 - 1
        for i in range(n,-1,-1):
            self.Heapfy(i)

    def insert(self,valor):
        if self.full():
            return "Heap cheio, Não e possivel inserir mais nada"
        self.vetor.append(valor)
        self.tamanhoheap += 1

    def imprime(self):
        print("\n",end="")
        for i in range(self.tamanhoheap):
            print(self.vetor[i],end=" ")
        print("\n")

    def heapsort(self):
        self.build_maxheap()
        n = self.tamanhoheap
        for i in range(n-1,0,-1):
            (self.vetor[i],self.vetor[0]) = (self.vetor[0],self.vetor[i])
            self.Heapfy(0,i)
