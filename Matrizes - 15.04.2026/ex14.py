import numpy as np


A = np.random.randint(1,10,(5,5))
print("matriz A:\n",A)
B = np.random.randint(1,10,(5,5))
print("Matriz B: \n",B)
C = A*B
print("Resultado da multiplicação de A por B:\n",C)