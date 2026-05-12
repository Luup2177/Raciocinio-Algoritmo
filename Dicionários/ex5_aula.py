dic = {"1" : 18 , "2" : 10 , "3" : 5 , "4" : 8}
print(dic)
decisao = str(input("Deseja apagar todos os dados ?(Y/N)"))
Y = decisao == "Y" == True
N = decisao == "N" == False
if decisao == True:
    dic.clear()
    print(dic)
else:
    print(dic)