p = float(input("Digite seu peso: "))
a = float(input("Digite sua altura:"))
IMC = p / (a**2)
if IMC > 25:
    print("Acima do peso ideial")
else:
    print("Peso dentro da normalidade")