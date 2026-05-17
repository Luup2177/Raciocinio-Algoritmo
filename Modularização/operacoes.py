numero = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
def soma():
    soma = numero + numero2
    print(soma)
    return soma
def sub():
    sub = numero - numero2
    if sub < 0:
        ao = sub*-1
        print(ao)
    else:
        print(sub)
    return sub
def multiplicar():
    multiplicar = numero * numero2
    print(multiplicar)
    return multiplicar
def dividir():
    divi = numero / numero2
    if divi == 0 :
        print("Divisao por zero!")
    else:
        print(divi)
    return divi