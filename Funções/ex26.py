def erro(n):
    return n * erro(n - 1)
# é uma função fatorial , onde não foi delcarado que se o valor for 1 ou 0 o resultado obtido será 1 , obtemos o erro de que por não ter essa decalaração a profunidade de itens se torna infinita