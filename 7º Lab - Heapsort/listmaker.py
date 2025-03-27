import random
def listmaker(n):
    vetor = []
    for _ in range(n):
        vetor.append(random.randrange(0,99))
    
    return vetor