user = {"luigi":18 , "leonildo": 48, "fabi":50 }
while True:
    sair = input("Quer sair? [S/N]")
    if sair == "s" or sair == "S":
        break
    else:
        print(user)
    operacao = str(input("O que vamos fazer hoje? ")).upper()
    if operacao == "E": #Exibir todos os usuários cadastrados
            qual = str(input("O que vc quer ver?"))
            if qual == "nomes":
             print(user.keys())
            elif qual == "idade":
             print(user.values())
            elif qual == "tudo":
             print(user.items())
            else:
             print("Essa opção não existe!")
    elif operacao == "B": #Buscar um usuário pelo nome usando.get()
        qual1 = str(input("Qual usuário vc quer ?"))
        if qual1 in user.keys():
         print(user.get(qual1))
        else:
            print("Este usuário não está no dicionário!")
    elif operacao == "A": #Adicionar um novo usuário
        novo_nome = str(input("Qual o novo nome a ser adicionado? "))
        novo_valor = int(input("Qual a idade do novo nome? "))
        user.update({novo_nome: novo_valor})
        print(user)
    elif operacao == "U": #Atualizar a idade de um usuário já existente
        print(user.keys())
        qual2 = str(input("Qual usuário terá sua idade alterada? "))
        nova_idade = int(input(f"Qual a idade nova de {qual2}? "))
        user.update({qual2: nova_idade})
        print(user)
    elif operacao == "R": #Remover usuário especifico
        print(user.keys())
        qual3 = str(input("Qual usuário será removido? "))
        excluido = user.pop(qual3)
        print(user)
    elif operacao == "L": #Remover o último usuário
        delete = str(input("Quer deletar o ultimo elemento inserido?"))
        if delete == "n":
            print(user)
        else:
         delet = user.popitem()
        print("O último elemento foi deletado :",user)
    elif operacao == "C": #Criar cópia e permite aterção em um dos valores para comparação
        copia = user.copy()
        print(copia)
        qual5 = str(input("Qual usuário terá sua idade alterada? "))
        nova_idad = int(input(f"Qual a idade nova de {qual5}? "))
        user.update({qual5: nova_idad})
        print("Alterado: ",user)
        print("Original: ",copia)
    elif operacao == "I":
    #Inicializa um novo dicionário com múltiplos usuários , utilizando .fromkeys()
    #idade padrão definida pelo usuário , deve ser informada uma lista de nomes separados por virgula
        novo = input("Qual o novo nome? ").split(",")
        novo = [n.strip() for n in novo]
        padrao = int(input("Qual o valor padrão para a lista?  "))
        usuarios = dict.fromkeys(novo , padrao)
        print(usuarios)
    elif operacao == "N":#Atualizar o dicionário principal com um dicionário informado pelo usuário
        novo_dic = {}
        qntd = int(input("Quantos itens deseja adicionar? "))
        for c in range(qntd ):
            chave = input(f"Digite a chave {c+1}: ")
            valor = input(f"Digite o valor {c+1}: ")
            novo_dic.update({chave:valor})
            user.update(novo_dic)
            print(user)
    elif operacao == "P": #Apaga o dicionário com clear
        apagar = input("Deseja realmente apagar o dicionário? [S/N]")
        if apagar == "S" or apagar == "s" :
            user.clear()
            print("Dicionário apagado: ",user)
        else:
            break
    elif operacao == "W": #Criar um novo dicionário usando .dict e uma lista de tuplas criada pelo usuário
        entrada = input("Tuplas no formato chave,valor (uma por linha). Digite 'fim' para encerrar:")
        lista_tuplas = []
        while True:
            linha = input("chave, valor (ou 'fim'): ")
            if linha.lower() == 'fim':
                break
            chave, valor = linha.split(",", 1)
            lista_tuplas.append((chave.strip(), valor.strip()))
        user = dict(lista_tuplas)
        print(user)