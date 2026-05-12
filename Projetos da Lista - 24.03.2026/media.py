cont = 0
soma_media = 0

while cont<3:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))

    media = (n1+n2+n3+n4)/4
    soma_media += media
    print("Média anual: ",media)

    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

        cont += 1
        media_total = soma_media / cont

    print(f"A média anual é: {media_total:.2f}")