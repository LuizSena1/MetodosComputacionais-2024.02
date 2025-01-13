def mdc(a,b): # Função do MDC, recebe dois numeros apenas a principio.
    while b != 0: # Mantem o loop enquanto o divisor não for 0.
        RESTO = a % b
        print(f'MDC : a = {a}, b = {b}')
        print(f'MDC : Resto = {RESTO}')
        a = b
        b = RESTO
    return a

def sequencia(n):
    if n <= 0:
        raise ValueError("A sequencia deve ser maior que zero")
    
    NUMBERS = []
    for i in range(n):
        NUMBER = int(input("Insira o Valor: "))
        while True:
            if NUMBER > 0:
                NUMBERS.append(NUMBER)
                break
            else:
                print("O valor dever ser positivo.")
            
    return NUMBERS


def calc_mdc(val):
    RESULT = val[0]
    for valor in val[1:]:
        RESULT = mdc(RESULT, valor)
        print(f'CALC MDC: RESULT = {RESULT}')
        print(f'CALC MDC: Valor = {valor}')
    return RESULT

while True:
    n = input("Insira o Valor de N: ")
    if n.isnumeric():
        n = int(n)
        break
    else:
        print("O valor N deve ser Numerico: ")

Numeros = sequencia(n)
Resposta = calc_mdc(Numeros)
print(f'O mdc da Sequencia {Numeros} e: {Resposta} ')