def leitura_matriz(linhas, formato):
    print(f"Insira as linhas da matriz com os elementos separados por espaços no formato {formato}\n")
    matriz = []
    for i in range(linhas):
        linha = list(map(int, input().split()))
        matriz.append(linha)
    return matriz

def exibir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == len(matriz[i]) - 1:
                print(matriz[i][j])
            else:
                print(matriz[i][j], end=" ")

# Exercício 16.1

def soma_linha_3(matriz):
    soma = 0
    for i in range(len(matriz[3])):
        soma = soma + matriz[3][i]
    return soma

def soma_coluna_2(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma = soma + matriz[i][2]
    return soma

def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma = soma + matriz[i][i]
    return soma

def soma_diagonal_secundaria(matriz):
    soma = 0
    for i in range(len(matriz) - 1, -1, -1):
        soma = soma + matriz[i][i]
    return soma

def soma_elementos(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma = soma + matriz[i][j]
    return soma

def exercicio_16_1():
    print("\n# Exercício 16.1\n") 
    matriz = leitura_matriz(5, "5x5")
    print("\na)", soma_linha_3(matriz))
    print("b)", soma_coluna_2(matriz))
    print("c)", soma_diagonal_principal(matriz))
    print("d)", soma_diagonal_secundaria(matriz))
    print("e)", soma_elementos(matriz))
    menu()

# Exercício 16.2

def soma_AB(matriz_A, matriz_B):
    matriz_S = []
    for i in range(len(matriz_A)):
        linha = []
        for j in range(len(matriz_A[i])):
            linha.append(matriz_A[i][j] + matriz_B[i][j])
        matriz_S.append(linha)
    return matriz_S

def diferenca_AB(matriz_A, matriz_B):
    matriz_D = []
    for i in range(len(matriz_A)):
        linha = []
        for j in range(len(matriz_A[i])):
            linha.append(matriz_A[i][j] - matriz_B[i][j])
        matriz_D.append(linha)
    return matriz_D

def exercicio_16_2():
    print("\n# Exercício 16.2\n")
    matriz_A = leitura_matriz(4, "4x6")
    print()
    matriz_B = leitura_matriz(4, "4x6")
    print("\na)") 
    exibir_matriz(soma_AB(matriz_A, matriz_B))
    print("\nb)") 
    exibir_matriz(diferenca_AB(matriz_A, matriz_B))
    menu()

# Exercício 16.3

def soma_canto_superior_esquerdo(matriz):
    soma = 0
    for i in range(2):
        for j in range(2):
            soma = soma + matriz[i][j]
    return soma

def soma_canto_inferior_direito(matriz):
    soma = 0
    for i in range(len(matriz) - 1, len(matriz) - 3, -1):
        for j in range(len(matriz[i]) - 1, len(matriz[i]) - 3, -1):
            soma = soma + matriz[i][j]
    return soma

def soma_triangulo_inferior(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(i + 1):
            soma = soma + matriz[i][j]
    return soma

def soma_triangulo_superior(matriz):
    soma = 0
    for i in range(len(matriz) - 1):
        for j in range(i + 1, len(matriz[i])):
            soma = soma + matriz[i][j]
    return soma

def exercicio_16_3():
    print("\n# Exercício 16.3\n")
    matriz = leitura_matriz(4, "4x4")
    print("\na)", soma_canto_superior_esquerdo(matriz))
    print("b)", soma_canto_inferior_direito(matriz))
    print("c)", soma_triangulo_inferior(matriz))
    print("d)", soma_triangulo_superior(matriz))
    menu()

# Exercício 16.4

def existe_valor(num, matriz):
    existe = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if num == matriz[i][j]:
                existe = True
                break
        if existe:
            break
    return existe

def exercicio_16_4():
    print("\n# Exercício 16.4\n")
    matriz = leitura_matriz(5, "5x5")
    num = int(input("\nInsira o valor desejado: "))
    existe = existe_valor(num, matriz)
    if existe:
        print(f"\nO número {num} existe na matriz\n")
    else:
        print(f"\nO número {num} não existe na matriz")
    menu()

# Exercício 16.5

def soma_linhas_colunas(matriz):
    linhas = [0] * len(matriz)
    colunas = [0] * len(matriz[0])
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            linhas[i] = linhas[i] + matriz[i][j]
            colunas[i] = colunas[i] + matriz[j][i]
    return linhas, colunas

def exercicio_16_5():
    print("\n# Exercício 16.5\n")
    matriz = leitura_matriz(5, "5x5")
    linhas, colunas = soma_linhas_colunas(matriz)
    print(f"\nSoma das linhas: {linhas}")
    print(f"Soma das colunas: {colunas}")
    menu()

# Exercício 16.6

def dividir_maior_elemento(matriz):
    for i in range(len(matriz)):
        maior = 0
        for j in range(len(matriz[i])):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
        for j in range(len(matriz[i])):
            matriz[i][j] = matriz[i][j] / maior
    return matriz

def exercicio_16_6():
    print("\n# Exercício 16.6\n")
    matriz = leitura_matriz(12, "12x13")
    print()
    exibir_matriz(dividir_maior_elemento(matriz))
    menu()

# Exercício 16.7

def loteria_esportiva(apostas, gabarito):
    pontos_totais = 0
    qte_apostas = [0] * 3
    for i in range(len(apostas)):
        pontos = 0
        for j in range(len(apostas[i])):
            if apostas[i][j] == 1 and gabarito[i] == j + 1:
                pontos_totais = pontos_totais + 1
            if apostas[i][j] == 1:
                pontos = pontos + 1
        if pontos != 0:
            qte_apostas[pontos - 1] = qte_apostas[pontos - 1] + 1
    return pontos_totais, qte_apostas

def exercicio_16_7():
    print("\n# Exercício 16.7\n")
    apostas = leitura_matriz(13, "13x3")
    print()
    gabarito = list(map(int, input("Insira o gabarito da loteria esportiva (com espaços): ").split()))
    pontos, qte_apostas = loteria_esportiva(apostas, gabarito)
    print(f"\nQuantidade total de pontos obtidos pelo jogador: {pontos}\n")
    print(f"Quantidade de apostas simples: {qte_apostas[0]}\n")
    print(f"Quantidade de apostas duplas: {qte_apostas[1]}\n")
    print(f"Quantidade de apostas triplas: {qte_apostas[2]}")
    menu()

# Exercício 17.1

def maior_elemento_linha(matriz):
    maiores = [0] * len(matriz)
    for i in range(len(matriz)):
        maior = 0
        for j in range(len(matriz[i])):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
        maiores[i] = maior
    return maiores

def exercicio_17_1():
    print("\n# Exercício 17.1\n")
    matriz = leitura_matriz(6, "6x6")
    maiores = maior_elemento_linha(matriz)
    print(f"\nOs maiores elementos de cada linha: {maiores}")
    menu()

# Exercício 17.2

def entre_colunas(matriz, coluna1, coluna2):
    pares = []
    for i in range(len(matriz)):
        for j in range(coluna1, coluna2 + 1):
            if matriz[i][j] % 2 == 0:
                pares.append(matriz[i][j])
    for k in range(len(pares)):
        if k == len(pares) - 1:
            print(pares[k])
        else:
            print(pares[k], end=", ")

def exercicio_17_2():
    print("\n# Exercício 17.2\n")
    matriz = leitura_matriz(4, "4x4")
    coluna1 = int(input("\nInforme a primeira coluna: "))
    coluna2 = int(input("Informe a segunda coluna: "))
    print(f"\nOs elementos pares presentes entre as colunas {coluna1} e {coluna2} (inclusive): ", end="")
    entre_colunas(matriz, coluna1, coluna2)
    menu()

# Exercício 17.3

def ordem_crescente(matriz):
    for j in range(len(matriz)):
        ordenado = False
        while not ordenado:
            ordenado = True
            for i in range(len(matriz[j]) - 1):
                if matriz[j][i] > matriz[j][i + 1]:
                    matriz[j][i], matriz[j][i + 1] = matriz[j][i + 1], matriz[j][i]
                    ordenado = False
    return matriz

def exercicio_17_3():
    print("\n# Exercício 17.3\n")
    matriz = leitura_matriz(5, "5x5")
    print()
    exibir_matriz(ordem_crescente(matriz))
    menu()

# Exercício 17.4

def trocar_par_impar(matriz):
    for i in range(len(matriz)):
        for j in range(0, len(matriz[i]), 2):
            matriz[i][j], matriz[i][j + 1] = matriz[i][j + 1], matriz[i][j]
    return matriz

def exercicio_17_4():
    print("\n# Exercício 17.4\n")
    matriz = leitura_matriz(6, "6x6")
    print()
    exibir_matriz(trocar_par_impar(matriz))
    menu()

# Exercício 17.5

def matriz_transposta(matriz):
    matriz_temp = []
    for k in range(len(matriz[0])):
        matriz_temp.append([0] * len(matriz))
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            matriz_temp[i][j] = matriz[j][i]
    return matriz_temp

def exercicio_17_5():
    print("\n# Exercício 17.5\n")
    linhas = int(input("Insira a quantidade de linhas: "))
    colunas = int(input("Insira a quantidade de colunas: "))
    matriz = leitura_matriz(linhas, f"{linhas}x{colunas}")
    print()
    exibir_matriz(matriz_transposta(matriz))
    menu()

# Exercício 17.6

def mais_populoso(matriz):
    soma = [0] * len(matriz)
    maior_c = 0
    cidade = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maior_c:
                maior_c = matriz[i][j]
                cidade = i
            soma[i] = soma[i] + matriz[i][j]
    maior = 0
    for k in range(len(soma)):
        if soma[k] > maior:
            maior = soma[k]
            indice = k
    return indice, cidade

def exercicio_17_6():
    print("\n# Exercício 17.6\n")
    matriz = leitura_matriz(4, "4x5")
    indice, cidade = mais_populoso(matriz)
    print(f"\nCódigo do estado mais populoso: {indice}")
    print(f"Código do estado que tem a cidade mais populosa: {cidade}")
    menu()

# Exercício 17.7

def exercicio_17_7():
    print("\n# Exercício 17.7\n")
    matriz = leitura_matriz(4, "4x4")
    print()
    cidade1 = int(input("Insira a primeira cidade: "))
    cidade2 = int(input("Insira a segunda cidade: "))
    print(f"\nA distância entre as cidades {cidade1} e {cidade2} é {matriz[cidade1][cidade2]}")
    menu()

# Exercício 17.8

def exercicio_17_8():
    print("\n# Exercício 17.8\n")
    matriz = leitura_matriz(4, "4x4")
    n = int(input("\nQuantidade de cidades que serão visitadas: "))
    codigo = list(map(int, input("Insira os códigos das cidades visitadas (com espaços): ").split()))
    distancia = 0
    for i in range(n - 1):
        distancia = distancia + matriz[codigo[i]][codigo[i + 1]]
    print(f"\nA distâcia total percorrida é {distancia}")
    menu()



def menu():
    print()
    print("*" * 30)
    print("\nEscolha um dos exercícios para executar:\n")
    print("| 16.1 | 16.2 | 16.3 | 16.4 | 16.5 | 16.6 | 16.7 |")
    print("| 17.1 | 17.2 | 17.3 | 17.4 | 17.5 | 17.6 | 17.7 | 17.8 |\n")
    print("Insira 0 se deseja finalizar o programa\n")
    escolha = input("Insira o número da questão como exibido nas opções: ")
    if escolha == "0":
        return
    elif escolha == "16.1":
        exercicio_16_1()
    elif escolha == "16.2":
        exercicio_16_2()
    elif escolha == "16.3":
        exercicio_16_3()
    elif escolha == "16.4":
        exercicio_16_4()
    elif escolha == "16.5":
        exercicio_16_5()
    elif escolha == "16.6":
        exercicio_16_6()
    elif escolha == "16.7":
        exercicio_16_7()
    elif escolha == "17.1":
        exercicio_17_1()
    elif escolha == "17.2":
        exercicio_17_2()
    elif escolha == "17.3":
        exercicio_17_3()
    elif escolha == "17.4":
        exercicio_17_4()
    elif escolha == "17.5":
        exercicio_17_5()
    elif escolha == "17.6":
        exercicio_17_6()
    elif escolha == "17.7":
        exercicio_17_7()
    elif escolha == "17.8":
        exercicio_17_8()
    else:
        print()
        print("*" * 30)
        print("\nOpção inválida!")
        print("Tente novamente...")
        menu()

menu()
