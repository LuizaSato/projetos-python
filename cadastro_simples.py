cadastros = []

while True:
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        cadastros.append(nome)
        print("Cadastro realizado.")

    elif opcao == "2":
        print("Cadastros:")
        for nome in cadastros:
            print(nome)

    elif opcao == "3":
        busca = input("Digite o nome para buscar: ")
        if busca in cadastros:
            print("Nome encontrado.")
        else:
            print("Nome não encontrado.")

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")
