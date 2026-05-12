import numpy as np


ingredientes = np.array ([
    [3,6,2],
    [8,4,7]
])
pedidos = np.array ([
    [65,5],
    [15,8],
    [14,15]
])
resultado = ingredientes @ pedidos
print("O resultado é igual a: \n",resultado)