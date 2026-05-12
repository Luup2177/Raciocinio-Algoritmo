dist = float(input("Quantos km são: "))
if dist<200.00:
    print(f"O preço é de: {dist * 0.5}")
else:
    print(f"O preço é de: {dist * 0.45}")