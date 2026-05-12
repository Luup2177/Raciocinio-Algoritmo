#Solicite ao usuário a entrada de 10 números inteiros;
#Armazene esses valores em uma lista chamada a.
a = []
for i in range(10):
   numero = int(input("Digite um número: "))
   a.append(numero)
#Considerando a lista a do exercício anterior, crie um programa que:
#Exiba todos os elementos da lista na tela;
#Mostre os valores um por linha.
print(a)
#Faça a lista informar o maior e o menor valor da lista
Min = min(a)
Max = max(a)
print("O maior valor da lista é: ", Max)
print("O menor valor da lista é: ", Min)
