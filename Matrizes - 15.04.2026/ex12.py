#verificação de simetria
#matriz = matriz transposta
import numpy as np


M = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
trans = M.T
print(M)
print(trans)
if M.all() == trans.all() :
    print("IGUAIS")
else:
    print("DIFERENTES")