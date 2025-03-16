import listar
import Crescente
from circular import ListaCircular
# test = int(input("Insira o numero desejado: "))
# for i in range(test):
#     ref = listar.insere(ref,i+1)
#     i += 1
# ref = None

# ref = Crescente.crescente(ref,1)
# ref = Crescente.crescente(ref,5)
# ref = Crescente.crescente(ref,90)
# ref = Crescente.crescente(ref,12)
# ref = Crescente.crescente(ref,44)
# listar.imprimir(ref)
# ref = listar.remover(ref,90)
# listar.imprimir(ref)
#test1 = int(input("Insira o Valor que deseja Retirar: "))
#listar.remover(ref,test1)
#listar.imprimir(ref)
#print(f"Removido valor: {test1}")
#ref = listar.limpar(ref) # Isso faz com que a Lista, seja limpa e fique vazia
#listar.imprimir(ref)
# ref = ListaCircular()

# ref.inserir(1)
# ref.inserir(2)
# ref.inserir(3)
# ref.inserir(4)
# ref.inserir(5)
# ref.inserir(6)
# ref.imprimir()
# ref.remover(6)
# ref.imprimir()
# ref.limpar()
# ref.imprimir()
f = ListaCircular()
for i in [1,2,3,4,5,6,7]:
        f.inserir(i)
f.endereços()