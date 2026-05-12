import numpy as np


notas = np.array([
    [85 ,92 ,78],
    [70 ,88 ,91],
    [62 ,75 ,80]
])
medias_alunos = np.mean(notas , axis=1)
print("Média por aluno:", medias_alunos)

medias_avaliacoes = np.mean(notas , axis=0)
print("Média pro avaliação:", medias_avaliacoes)
