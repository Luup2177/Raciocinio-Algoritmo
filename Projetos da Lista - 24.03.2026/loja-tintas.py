area = float(input("Qual a área a ser pintada? (em metros quadrados): "))
# 1L de tinta cobre 3m²
# A lata de tinta de 18L custa 80 reais
# informe ao usuário quantas latas ele precisa
litro = area/3
print(f"Você vai precisar de {litro:.2f} litros de tinta")
qntd_latas = area/(18*3)
print(f"Você vai precisar de {qntd_latas:.2f} latas de tinta")
gasto = qntd_latas * 80
print(f"Você vai gastar {gasto:.2f} reais para pintar essa área")