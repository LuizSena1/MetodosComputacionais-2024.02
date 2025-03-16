
class lista: # Inicia e cria a class lista que sera usada depois.
    def __init__(self,info = None,prox = None):
        self.info = info # Define a informação
        self.prox = prox # Aponta o proximo valor/casa/No

def insere(ref, valor):
    n_no = lista(valor) # Define o novo no como o valor dado.
    n_no.prox = ref # Define o proximo No, como o valor que anteriormente era a casa inicial ou ref.
    return n_no # Retorna a mudança.


def imprimir(ref): # Função para imprimir a Lista independende de seu tamanho.
    p = ref
    #print("Imprimindo a Lista:")
    print("\n| Imprimindo Lista:",end=" ")
    if(ref is None):
        return print("Lista Vazia")
    while p:
        print(p.info, end=" ") # Faz o print ta casa/No atual
        p = p.prox # E passa para o proximo no
    print("|")

def remover(ref, valor):
    ant = None
    busca = valor
    p = ref
    while(p != None and p.info != busca):
        ant = p
        p = p.prox

    if (p == None):
        return ref
    
    if (p == ref):
        ref = p.prox

    else:
        ant.prox = p.prox
    return ref

def limpar(ref):
    p = ref
    while ref is not None:
        p = ref.prox # Define o ponto p.info como ref.prox para que o ciclo continue ate o ultimo no da lista
        ref.prox = None # "Apaga" o proximo No da lista. 
        ref = p 
    return ref

def enderecos(ref):
    if ref is None:
       return print("Lista Vazia...")
    
    p = ref
    print("Imprimindo Lista com seus Endereços de Memoria: ")
    while p:
        print(f"Elementos : {p.info}, Endereço na Memoria: {id(p.info)}") # Exibe lado a lado os valores e seus endereços.
        p = p.prox

def duplicados(ref):
    if ref is None:
        return print("Lista esta Vazia")
    
    p = ref # Define o ponteiro do Nó atual
    while p != None:
        ant = p # Ponteiro para o nó anterior
        aux = p.prox # Ponteiro auxiliar para proximo no.

        while aux != None: # Ira percorrer os items a frente com intuito de eliminar copias.
            if aux.info == p.info: # If para encontrar um valor duplicado
                ant.prox = aux.prox # Quando valor e encotnrado, ele e removido.
            else: # Caso não seja encontrado um valor duplicado
                ant = aux  # Apenas atualiza o ponteiro
            aux = aux.prox # E passa para o proximo nó

        p = p.prox  # Mesma coisa, passa para o proximo nó

    return ref