def filtrar_funcionarios(funcionarios, cargo):
  lista = []
  for funcionario in funcionarios:
    if funcionario["cargo"] == cargo:
      lista.append(funcionario["nome"]) 
   
  return lista

# Função para entrada do usuário
def main_filtro():
    n = int(input())
    funcionarios = []

    for _ in range(n):
        id_funcionario = int(input())
        nome = input()
        cargo = input()
        funcionarios.append({"id": id_funcionario, "nome": nome, "cargo": cargo})

    cargo_filtro = input()
    resultado = filtrar_funcionarios(funcionarios, cargo_filtro)
    
    print(resultado)

# Executando a função
main_filtro()