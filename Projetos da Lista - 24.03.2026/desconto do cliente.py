preco = float(input("Valor da compra: "))
if preco > 100.00:
    print(f"O preço final foi de: {preco * 0.9}")
else :
    print("O valor da conta é:",preco,)
    print("Nas compras acima de R$:100.00 , você ganha 10% de desconto!")