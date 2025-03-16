from PilhaEncadeada import pilha


def verifica_parenteses(expresso):
    pil = pilha()

    for char in expresso: # Roda a expressão inteira.

        if char == "(": # Quando registra quando parentese e aberto
            pil.push(char) # E o coloca na pilha
        
        elif char == ")": # Registra quando o parentese e fechado 
            if pil.empty(): # Checa se a pilha esta vazia. Se tiver significa que o parentese foi posto indevidamente
                return False # Retorna falso
            pil.pop() # Caso não vazio, Retira o parentese que estava na pilha, a fazendo ser vazia.
    return pil.empty() # Quando termina a expressão, Roda o .empty() para checar se a pilha esta vazia. Se estiver, significa que se teve uma expressão correta.

