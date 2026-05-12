import numpy as np


antes = np.array([
    [1,2,3,4,5,],
    [6,7,8,9,10,],
    [11,12,13,14,15,],
    [16,17,18,19,20,],
    [21,22,23,24,25],
])
print("Matriz original: \n",antes,"\n")
antes[3][1] = 92
antes[4][3] = 91
print("Matriz alterada: \n",antes,"\n")