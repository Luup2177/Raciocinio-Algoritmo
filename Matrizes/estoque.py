import numpy as np



estoqueinicial= np.array ([
    [10,11,12],
    [13,14,15],
    [16,17,18],
])
vendidos = np.array ([
    [1,2,3],
    [4,5,6],
    [7,8,9],
])

estoque_final = estoqueinicial - vendidos
print("Estoque final: ",estoque_final)
print("Etoque inicial: ",estoqueinicial)
print("Vendidos: ",vendidos)