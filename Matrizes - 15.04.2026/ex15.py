#criando a matriz
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
linhas = len(matriz)
colunas = len(matriz[0])
print("Matriz original:\n",matriz)
# rodando a matriz em 90º no sentido horário
transposta = [[matriz[i][j]for i in range(colunas)] for j in range(linhas)]
print(transposta)