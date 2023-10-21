def initial_message():
    print ("------------------------------------------------------")
    print ("ESTA É UMA SIMULAÇÃO DE PILHA DE LIVROS NA PRATELEIRA!")
    print ("------------------------------------------------------")
    print ("Este programa permite que você organize e visualize uma pilha de livros em uma prateleira.")
    print ("Você pode adicionar livros, removê-los, ver o livro no topo e muito mais.")
    print ("")

initial_message()

shelf = []

while True:
    print ("Use as opções a seguir para interagir com a prateleira de livros:")
    print ("1. Empilhar livro")
    print ("2. Desempilhar livro")
    print ("3. Mostrar livro no topo da prateleira")
    print ("4. Listar todos os livros empilhados")
    print ("5. Limpar prateleira")
    print ("6. Sair do programa")
    print ("------------------------------------------------------")
    option = input("Insira a opção desejada:")
    print ("------------------------------------------------------")

    if option == '1':
        book = input("Qual livro deseja empilhar na prateleira?")
        shelf.append(book)
        print ("Seu livro foi empilhado!")
    elif option == '2':
        if not shelf:
            print ("A prateleira está vazia! Não é possível desempilhar um livro dela.")
        else: 
            shelf.pop()
            print ("O último livro da prateleira foi desempilhado!")
    elif option == '3':
        if not shelf:
            print ("A prateleira está vazia! Não há livro no topo.")
        else:
            element_top = shelf[-1]
            print (element_top)
    elif option == '4':
        if not shelf:
            print ("A prateleira está vazia! Não há livros empilhados.")
        else:
            for book in shelf:
                print (book)
    elif option == '5':
        if not shelf:
            print ("Não há livros na prateleira, portanto, ela já se encontra limpa!")
        else: 
            shelf.clear()
    elif option == '6':
            print ("Simulação encerrada. Volte sempre!")
            break
    else: 
        print ("Opção inválida! Insira uma das opções disponíveis no Menu")
    