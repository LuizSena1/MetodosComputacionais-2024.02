import listar
import random

ref = None
listar.limpar(ref)
for i in range(10):
    ref = listar.insere(ref, i + 1)

listar.enderecos(ref)