import numpy as np
#Cidade = porto
#Regiões = norte , sul , leste
#Chuva em mm
manha = np.array([
    [81,72,39],
    [72,19,74],
    [92,16,15]
])
tarde = np.array([
    [91,35,64],
    [61,52,39],
    [36,17,40]
])
soma = manha + tarde
manha1 = np.sum(manha)
tarde1 = np.sum(tarde)
somas = np.sum(soma)
print(F"De manhã choveu ", manha1 , "mm", manha)
print(F"De tarde choveu ", tarde1 , "mm" , tarde)
print(F"Ao todo choveram ",somas ,"mm", soma)