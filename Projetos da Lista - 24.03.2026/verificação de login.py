user_correct = "admin"
user = str(input("Insira o usuário: ")) .lower() .strip()
if user == user_correct:
    print("Acesso concedido!")
else :
    print("Usuário  desconhecido")