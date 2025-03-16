from fila import Fila
from FilaTam import TFila
from Soma import soma
from intercala import intercal
from FilaSimul import simulation
# fila = Fila()

# for i in [1,2,3,4,5]:
#     fila.push(i)

# fila.display()

# fila.rotate(120)

# f1 = TFila(5)
# f2 = TFila(5)

# for i in [1,2,3,4,5,6,7]:
#     f1.push(i)

# for i in [6,7,8,9,10]:
#     f2.push(i)

# f1.display()
# f2.display()

# som = soma(f1,f2)
# som.display()

# teste = Fila()
# for i in [1,2,3,4,5]:
#     teste.push(i)

# teste.display()
# teste.inverte()

# t1 = Fila()
# t2 = Fila()

# for i in [1,3,5,7,9]:
#     t1.push(i)

# for i in [2,4,6,8]:
#     t2.push(i)

# t1.display()
# t2.display()
# r = intercal(t1,t2)
# r.display()

fila = simulation()

fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)
print(fila.dequeue())
print(fila.dequeue())
print(fila.peek())
fila.display()