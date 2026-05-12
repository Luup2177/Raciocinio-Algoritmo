import numpy as np


matriz = np.random.randint(0,1000,(3,3))
print(matriz)
media1 = np.mean(matriz , axis=0)
print(media1)