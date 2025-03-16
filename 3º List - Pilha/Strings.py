from PilhaEncadeada import pilha

def inverter(palavra):
    pil = pilha()

    for letra in palavra: # Cria uma pilha, usando cada letra na string informada.
        pil.push(letra)
    
    invertida = ""
    while not pil.empty(): # Mantem o codigo rodando enquanto pil não for nula
        invertida += pil.pop() # Usa o pop para ir retirando as letras, como pilha funciona a base de First in last out. As ultimas letras saem primeiro.
    
    return invertida # String invertida criada e retornada.

def palindromo(palavra):
    pil = pilha()
    organizada = "".join(letra.lower() for letra in palavra)
    # print(organizada)
    for letra in palavra:
        pil.push(letra)

    invertida = ""
    while not pil.empty(): # Mantem o codigo rodando enquanto pil não for nula
        invertida += pil.pop()
    
    invertida = "".join(letra.lower() for letra in invertida) # Apenas para manter tudo organizado, sem que lower ou upper case cause problemas.
    return organizada == invertida

test1 = "ReNnEr"
test2 = "oVO"
test3 = "RadAr"
t1 = palindromo(test1)
t2 = palindromo(test2)
t3 = palindromo(test3)
print(t1)
print(t2)
print(t3)