def calculadora(a,b,operacao):
    if operacao == '+':
        return a+b
    elif operacao == '-':
        return a-b
    elif operacao == '*':
        return a*b
    elif operacao == '/':
        if b ==0:
                return "Erro: divisão por zero!"
        return a/b
    else:
        return "Erro: operacao invalida!"