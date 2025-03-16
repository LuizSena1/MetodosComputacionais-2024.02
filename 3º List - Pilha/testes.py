from PilhaVetor import pilhavetor

pilha = pilhavetor(5)
pilha.push(10)
pilha.push(20)
pilha.push(30)

print(f"Topo: {pilha.peek()}")
print(f"Elemento removido: {pilha.pop()}")
print(f"Pilha apos Remover: {pilha.peek()}")

teste = pilhavetor(3)
teste.push(10)
teste.push(10)
teste.push(10)
teste.push(20)