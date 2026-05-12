import numpy as np


matriz = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])
valor = int(input("Digite um valor: "))
if valor in matriz :
    print("O valor digitado está na matriz!")
else :
    print("O valor não está na matriz!")