import listar
def crescente(ref,valor):
    n_no = listar.lista(valor)
    aux = ref # Serve para auxiliar na resolução.

    if ref == None: # Apenas para fazer que caso seja o primeiro Valor da lista, o codigo passe.
        n_no.prox = ref
        return n_no
    
    while aux.prox != None and aux.prox.info < valor:
        aux = aux.prox

    n_no.prox = aux.prox # N_no apota para o promximo nó
    aux.prox = n_no # o nó anterior aponta para o novo nó.
    # Essa parte serve para inserir o valor no ponto correto e colocando os numeros em suas devidas casas. 
    return ref