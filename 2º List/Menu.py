import listar 

lista = None
while True:
    print("\nMenu")
    print("1. Inserir")
    print("2. Imprimir")
    print("3. Remover")
    print("4. Limpar")
    print("5. Remover Numeros repetidos")
    print("Any Key. Finalizar Programa")

    escolha = input("Escolha a Opção desejada: ")
    valor = 0
    match escolha:
        case "1":
            valor = int(input("Digite o Valor a ser Inserido: "))
            lista = listar.insere(lista,valor) 
            
        case "2":
            listar.imprimir(lista)

        case "3":
            valor = int(input("Digite o valor a ser Removido: "))
            lista = listar.remover(lista,valor)
            
        case "4":
            lista = listar.limpar(lista)

        case "5":
            lista = listar.duplicados(lista)

        case default:
            print("Finalizando Programa...")
            break
