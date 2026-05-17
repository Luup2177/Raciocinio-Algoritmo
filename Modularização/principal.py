import usuario
import operacoes

qual = int(input("Qual Processo vai ser realizado ? (1 = Operações , 2= Usuário )"))
if qual == 1 :
    qual2 = int(input("Qual Processo vai ser realizado ? (1 = Soma , 2= Subtração , 3=Multiplicação , 4=Divisão )"))
    if qual2 == 1:
        operacoes.soma()
    elif qual2 == 2:
        operacoes.sub()
    elif qual2 == 3:
        operacoes.multiplicar()
    elif qual2 == 4:
        operacoes.dividir()
elif qual == 2 :
    nome = input("Qual o seu nome?")
    usuario.registro(nome)
    usuario.ola(nome)