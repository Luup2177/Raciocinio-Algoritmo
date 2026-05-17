texto = str
Lista = []
def comprimento():
        contagem = str(input("Digite A palavra ou a frase que será contada:"))
        comprido = len(contagem.replace(" ", ""))
        print(f"{contagem} tem {comprido} caracteres")
def aumentar(texto):
    print("O texto em maiusculo fica assim:",texto.upper())
    return texto
