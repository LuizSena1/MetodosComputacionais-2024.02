print("Bem vindo")
while True:
    a = input("Insira o Primeiro valor: ")
    b = input("Insira o Segundo valor: ")
    if a.isnumeric() and b.isnumeric():
        a = int(a)
        b = int(b)
        break
    else:
        print("Porfavor insira Apenas Numeros inteiros")
if a != b:
    if a > b:
        print("A e maior")
    else:
        print("B e maior")
else:
    print("Esses numeros são iguais")

    

