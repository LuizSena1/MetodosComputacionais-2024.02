print("Bem vindo")

def Soma(a,b,c):
    return a+b+c

def multi(a,b,c):
    return a*b*c

def media(a,b,c):
    return (a+b+c)/3

def maiormenor(a,b,c):

    if a > b and a > c:
        maior = a
    elif b  > a and b > c:
        maior = b
    else:
        maior = c

    if a < b and a < c:
        menor = a
    elif b < a and b < c:
        menor = b
    else: 
        menor = c

    return maior, menor

while True:
    a = input("Insira o Primeiro valor: ")
    b = input("Insira o Segundo valor: ")
    c = input("Insira o Terceiro Valor: ")
    if a.isnumeric() and b.isnumeric() and c.isnumeric():
        a = int(a)
        b = int(b)
        c = int(c)
        break
    else:
        print("Porfavor insira Apenas Numeros inteiros")

som = Soma(a,b,c)
med = media(a,b,c)
prod = multi(a,b,c)
maior,menor = maiormenor(a,b,c)
print(f"A soma dos valores e {som}")
print(f"A media dos valores e {med}")
print(f"O produto dos valores e {prod}")
if maior != menor:
    print(f"O maior valor e {maior}, o menor valor {menor}")