# Lista para armazenar o nome dos alunos
alunos = []
nAlunos = int(input("Quantos alunos tem na turma? "))

#Loop para ler os nomes dos alunos
for i in range (nAlunos):
    nome = input(f"Qual o nome do aluno? ")
    alunos.append(nome)
print("Os alunos da turma são: ", alunos)
for nome in alunos:
    print(nome)