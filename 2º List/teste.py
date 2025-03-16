def calcular_salarios(funcionarios):
    salarios = []
    for funcionario in funcionarios:
        salario = funcionario["horas"] * funcionario["valor"]
        salarios.append(f"{funcionario["nome"]}: {salario:.2f}")
    return salarios

    # TODO: Calcule os salários com base nas horas trabalhadas e no valor por hora:
    
    #TODO: Retorne 'salarios':
    

# Função para entrada do usuário
def main_salario():
    n = int(input())
    funcionarios = []

    for _ in range(n):
        nome = input()
        horas_trabalhadas = int(input())
        valor_hora = float(input())
        funcionarios.append({"nome": nome, "horas": horas_trabalhadas, "valor": valor_hora})
        # TODO: Adicione um dicionário com as informações do funcionário à lista 'funcionarios'.
        

    resultado = calcular_salarios(funcionarios)
    
    for salario in resultado:
        print(salario)

# Executando a função
main_salario()