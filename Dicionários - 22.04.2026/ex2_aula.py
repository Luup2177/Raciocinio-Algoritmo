dic = {"1" : 19.90 , "2" : 20.75 , "3" : 30.75}
print(dic)
produto = input("Qual produto terá o preço alterado ?")
np = float(input(f"Qual o novo preço do {produto}?"))
dic[produto] = np
print(dic)
