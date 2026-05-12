import numpy as np


number = 1
matriz = np.random.randint(0,100,(5,5))
print("matriz principal :\n",matriz)
iden = np.identity(5)
print("Diagonal principal :\n",iden)
sla = matriz*iden
print("Diagonal principal com os itens da matriz : \n",sla)
iden1 = (iden - 1)*-1
print(iden1)
multiplicacao = iden1*matriz
print(multiplicacao)
#COMO QUE FAZ PRA ZERAR A DIAGONAL PRINCIPAL CARALHO SOCORROOOOOOOOO
#Consegui :D (mas o zero ficou negativo por algum motivo)
