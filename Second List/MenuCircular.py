from circular import ListaCircular
lista = ListaCircular()
while True:
    print("\nMenu")
    print("1. Inserir")
    print("2. Imprimir")
    print("3. Remover")
    print("4. Limpar")
    print("5. Finalizar Programa")

    escolha = input("Escolha a Opção desejada: ")
    valor = 0
    match escolha:
        case "1":
                valor = int(input("Digite o Valor a ser Inserido: "))
                lista.inserir(valor) 
            
        case "2":
                lista.imprimir()

        case "3":
                valor = int(input("Digite o valor a ser Removido: "))
                lista.remover(valor)
            
        case "4":
                lista.limpar()

        case default:
                print("Finalizando Programa...")
                break