def fatorial(n):
    RESULT = 1
    i = 1
    if n < 2:
        return RESULT
    while i < n+1:
        RESULT *= i
        i += 1
    return RESULT

while True:
    n = input("Insira o Valor de N: ")
    if n.isnumeric():
        n = int(n)
        break
    else:
        print("Insira Numero Inteiro")

RESPOSTA = fatorial(n)
print(RESPOSTA)