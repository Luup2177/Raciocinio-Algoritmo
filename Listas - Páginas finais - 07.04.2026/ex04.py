#Solicite a quanidade de alunos na turma
qntd = int(input("Quantos alunos tem na turma? "))
#Em seguida leia a nota de cada aluno ( valores inteiros de 0 a 100 )
notas = []
aluno_aprovado = 0
aluno_reprovado = 0
for i in range(qntd):
    nota = int(input(f"Qual a nota do aluno {i+1}? "))
    if 0<=nota<=100:
        notas.append(nota)
        if nota >= 60:
            aluno_aprovado += 1
        else:
            aluno_reprovado += 1
    else:
        print("O número de alunos aprovados é: ", aluno_aprovado)
        print("O número de alunos reprovados é: ", aluno_reprovado)
        if nota > 100:
            print("Insira uma nota entre 0 e 100!\n""Tente novamente")
            break
#armazene as notas em uma lista
media = 60
# Mostre quantos alunos estão abaixo da média e quantos alunos estão acima da média


