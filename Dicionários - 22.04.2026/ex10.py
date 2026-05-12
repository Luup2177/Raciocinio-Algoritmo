dic = {"chico" : 4 , "maria" : 10 , "juli": 8 , "joão" : 7 , "mario" : 2}
print(dic)
delete = str(input("Digite o nome para deletar: "))
if delete in dic:
    dic.pop(delete)
    print(dic)
chave_pop, valor_pop = dic.popitem()
print(f"\n Popitem() removeu o último item → '{chave_pop}: {valor_pop}'")
print(dic)

nome = input("Digite um novo nome para substituir: ").strip()
valor = int(input("Digite o valor do nome para substituir: "))
dic[nome] = valor
print(dic)

