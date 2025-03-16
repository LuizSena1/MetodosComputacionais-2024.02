def fibonacci(n):
    SOMA = 0
    A = 1
    B = 1
    i = 0
    if n < 3:
        return 1
    while i < (n-2):
        SOMA = A + B
        B = A
        A = SOMA
        i += 1
    return SOMA

n = int(input("Insira o Valor de N: "))
resposta = fibonacci(n)
print(resposta)