from Cliente import atendimento
fila = atendimento()

while True:
    print("\n Porfavor, escolha a Opção desejada:")
    print("1 - Adicionar um Novo cliente.")
    print("2 - Remover Cliente atendido.")
    print("3 - Mostrar Fila de Atendimento.")
    print("4 or Any key - Encerra o Programa.")

    escolha = input("Seleção: ")
    match escolha:
        case "1":
            nome = input("Digite o Nome do Cliente: ")
            fila.inserir(nome)

        case "2":
            print("Removendo Cliente em Atendimento...")
            fila.atendido()
            print("...Cliente Removido")
        
        case "3":
            print("Buscando Dados...")
            print("Dados Encontrados")
            fila.imprimir()
        
        case default:
            print("Encerrando o Progama...")
            print("Ate Mais")
            break