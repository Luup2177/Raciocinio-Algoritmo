def AreaQuadrado():
    L = int(input("Qaunto vale o lado do quadrado? "))
    print("O valor do lado do quadrado: ", L)
    A = L**2
    print(f"A área do quadrado é {A}")
    return A
def AreaCirculo():
    R = int(input("Qual o valor do raio do circulo? "))
    print("O valor do raio do circulo: ", R)
    A2 = (R**2)*3.14
    print("O valor da área do circulo: ", A2)
    return A2
def PerimetroRetangulo():
    B = int(input("Qual o valor da base? "))
    H = int(input("Qual o valor da altura? "))
    P = 2*(B+H)
    print(f"O valor do perímetro do retangulo com base {B} e altura {H} é de {P}")