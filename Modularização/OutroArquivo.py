import geometria

qual = input("Qual Processo vai ser realizado ? (Q = quadrado , C= circulo , R= retangulo)").upper()
if qual == "Q":
    geometria.AreaQuadrado()
elif qual == "C":
    geometria.AreaCirculo()
elif qual == "R":
    geometria.PerimetroRetangulo()
