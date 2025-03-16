def Soma(a,b):
    return a+b

def subtra(a,b):
    return a-b

def multi(a,b):
    return a*b

def divi(a,b):
    return a/b

while True:
    OPERA = ["+","-","*","/"]
    A = input("Escolha uma das Operações: [+ , - , / , *]")
    if A in OPERA:
        while True:
            n1 = input("Insira o primeiro Numero:")
            n2 = input("Insira o segundo Numero: ")
            if n1.isnumeric() and n2.isnumeric():
                n1 = int(n1)
                n2 = int(n2)
                break
            else:
                print("Insira apenas Valores Inteiros")
                
        if A == "/":
            if n2 == 0:
                raise ValueError("Não se pode Dividir por 0")
            RESPOSTA = divi(n1,n2)
            print(f'{n1} / {n2} = {RESPOSTA}')
        if A == "+":
            RESPOSTA = Soma(n1,n2)
            print(f'{n1} + {n2} = {RESPOSTA}')
        if A == "-":
            RESPOSTA = subtra(n1,n2)
            print(f'{n1} - {n2} = {RESPOSTA}')
        if A == "*":
            RESPOSTA = multi(n1,n2)
            print(f'{n1} * {n2} = {RESPOSTA}')
    else:
        raise ValueError("Operação Invalida")

    C = input("Continuar? [S] [N] ")
    C = C.upper()

    if C == "N":
        break