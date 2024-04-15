#Faça um programa que leia uma matriz 3x3 de inteiros e multiplique os elementos da diagonal principal da matriz por um número k. Imprima a matriz na tela antes e depois da multiplicação.

def matriz_3x3():
    # Inicializa uma matriz 3x3 vazia
    matriz = []
    print("Digite os elementos da matriz 3x3:")

    # Lê os valores da matriz 3x3 do usuário
    for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input(f"Digite o valor para a posição ({i+1}, {j+1}): "))
            linha.append(valor)
        matriz.append(linha)

    return matriz

def copiar(matriz):
    # Cria uma cópia da matriz original
    copia = []
    for linha in matriz:
        copia.append(linha[:])  # Copia cada linha da matriz original
    return copia

def imprimir(matriz,largura=3):
    # Percorre a matriz e imprime seus valores em forma de matriz
    for linha in matriz:
        # Formata cada elemento da linha para ter a largura especificada
        elementos_formatados = [f"{elemento:{largura}d}" for elemento in linha]
        # Junte os elementos formatados com um espaço e imprima a linha
        print(" ".join(elementos_formatados))

def diagonal_principal(matriz, k):
    # Multiplica os elementos da diagonal principal por k
    for i in range(3):
        matriz[i][i] *= k

def diagonal_secundaria(matriz, k):
    # Multiplica os elementos da diagonal secundaria por k
    for i in range(3):
        j=2-i
        matriz[j][i] *= k

def main():
    # Lê a matriz 3x3 do usuário
    matriz = matriz_3x3()
    # matriz = [[1, 2,3], [4, 5, 6],[7,8,9]] #teste
    matriz0=copiar(matriz)

    # Imprime a matriz antes da multiplicação
    print("\nMatriz antes da multiplicação:")
    imprimir(matriz)

    while True:
        qual=input("""\nVocê deseja mutiplicar:
1)Só a diagonal principal
2)Só a diagonal secundaria
3)Ambas as diagonais           
\nDigite  o numero da opção que você quer fazer:""")
        
        if(qual=='1'):

            # Lê o valor de k do usuário
            k = int(input("Digite o valor de k para multiplicar a diagonal principal: "))

            # Multiplica a diagonal principal por k
            diagonal_principal(matriz, k)

            # Imprime a matriz depois da multiplicação
            print("\nMatriz depois da multiplicação da diagonal principal:")
            imprimir(matriz)
            break

        elif(qual=='2'):

            k = int(input("\nDigite o valor de k para multiplicar a diagonal secundaria: "))
            #restaura a matriz
            matriz=copiar(matriz0)

            # Multiplica a diagonal secundaria por k
            diagonal_secundaria(matriz, k)

            # Imprime a matriz depois da multiplicação
            print("\nMatriz depois da multiplicação da diagonal secundaria:")
            imprimir(matriz)
            break

        elif(qual=='3'):
            # Lê o valor de k do usuário
            k = int(input("Digite o valor de k para multiplicar a diagonal principal: "))

            # Multiplica a diagonal principal por k
            diagonal_principal(matriz, k)

            # Imprime a matriz depois da multiplicação
            print("\nMatriz depois da multiplicação da diagonal principal:")
            imprimir(matriz)

            k = int(input("\nDigite o valor de k para multiplicar a diagonal secundaria: "))
            #restaura a matriz
            matriz=copiar(matriz0)

            # Multiplica a diagonal secundaria por k
            diagonal_secundaria(matriz, k)

            # Imprime a matriz depois da multiplicação
            print("\nMatriz depois da multiplicação da diagonal secundaria:")
            imprimir(matriz)
            break
        else:
            print("Esse não é um valor valido,digite um valor valido")
            continue

# Chama a função principal para iniciar o programa
main()
