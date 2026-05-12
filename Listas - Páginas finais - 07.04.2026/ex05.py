#Solicite ao usuário a entrada de 5 números inteiros;
num = []
for i in range(5):
    pedir = int(input("Digite um número: "))
# Armazene esses valores em uma lista;
    num.append(pedir)
# Ao final, determine e exiba:
# O maior número par da lista (caso exista);
Maxpar = max(num) % 2 == 0
# O menor número ímpar da lista (caso exista);
Minimpar = min(num) % 2 != 0
# O somatório de todos os elementos da lista;
print(f"O somatório total dos valores é igual a: {sum(num)}")
# A média dos valores.
print(f"A média dos valores é igual a: {sum(num)/len(num):.2f}")
# Caso não existam números pares ou ímpares, exiba uma mensagem apropriada
if Minimpar == False :
    print("Não existem números impares na lista!")
elif Maxpar == False :
    print("Não existem números pares na lista!")
