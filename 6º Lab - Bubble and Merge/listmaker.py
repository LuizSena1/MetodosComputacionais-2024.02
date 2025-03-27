import random
def listmaker(n):
    vetor = []
    for _ in range(n):
        vetor.append(random.randrange(0,999))
    
    return vetor