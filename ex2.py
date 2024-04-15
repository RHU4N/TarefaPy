#Faça um programa que leia duas matrizes A e B 2x2 de inteiros e imprima a matriz C que é a soma das matrizes A e B.

def matriz_2x2(nome):
    matriz = []
    print(f"Digite os elementos da matriz {nome}:")
    for i in range(2):
        linha = []
        for j in range(2):
            valor = int(input(f"Digite o valor para a posição ({i+1}, {j+1}) da matriz {nome}: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def soma(A, B):
    C = []
    for i in range(2):
        linha = []
        for j in range(2):
            # Calcula a soma dos elementos correspondentes de A e B
            soma = A[i][j] + B[i][j]
            linha.append(soma)
        C.append(linha)
    return C

def copiar(matriz):
    # Cria uma cópia da matriz original
    copia = []
    for linha in matriz:
        copia.append(linha[:])  # Copia cada linha da matriz original
    return copia

def subtracao(A, B):
    C = []
    for i in range(2):
        linha = []
        for j in range(2):
            # Calcula a soma dos elementos correspondentes de A e B
            sub = A[i][j] - B[i][j]
            linha.append(sub)
        C.append(linha)
    return C

def imprimir(matriz,largura=4):
    # Percorre a matriz e imprime seus valores em forma de matriz
    for linha in matriz:
        # Formata cada elemento da linha para ter a largura especificada
        elementos_formatados = [f"{elemento:{largura}d}" for elemento in linha]
        # Junte os elementos formatados com um espaço e imprima a linha
        print(" ".join(elementos_formatados))

def main():
    # Ler as matrizes A e B do usuário
    matriz_A = matriz_2x2("A")
    matriz_B = matriz_2x2("B")
    # matriz_A = [[1, 2], [4, 5]] # teste
    # matriz_B = [[1, 2], [4, 5]] #teste

    print('\nEssa á a matriz A:')
    imprimir(matriz_A)
    print('\nEssa á a matriz B:')
    imprimir(matriz_B)

    while True:
            qual=input("""\nVocê deseja:
    1)Somar
    2)Subtrair
    3)Ambas operações           
    \nDigite  o numero da opção que você quer fazer:""")
            
            if(qual=='1'):

                # Calcular a soma das matrizes A e B
                matriz_C = soma(matriz_A, matriz_B)
                # Imprimir a matriz C
                print("\nMatriz C que é a soma de A e B:")
                imprimir(matriz_C)
                break

            elif(qual=='2'):

                matriz_C = subtracao(matriz_A,matriz_B)
                print("\nMatriz C que é a subtração de A e B:")
                imprimir(matriz_C)
                break

            elif(qual=='3'):
                # Calcular a soma das matrizes A e B
                matriz_C = soma(matriz_A, matriz_B)
                # Imprimir a matriz C
                print("\nMatriz C que como a soma de A e B:")
                imprimir(matriz_C)

                matriz_C = subtracao(matriz_A,matriz_B)
                print("\nMatriz C que como a subtração de A e B:")
                imprimir(matriz_C)

                break
            
            else:
                print("Esse não é um valor valido,digite um valor valido")
                continue

# Chama a função principal para iniciar o programa
main()
