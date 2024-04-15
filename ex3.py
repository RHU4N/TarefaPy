#Faça um programa que leia as dimensões de duas matrizes A e B, e depois leia as duas matrizes (os elementos devem ser inteiros). Se as matrizes forem de tamanhos compatíveis para multiplicação, multiplique as matrizes. Imprima as matrizes A, B e a matriz resultante da multiplicação.

def ler_matriz(linhas, colunas, nome): #Nome=A ou B colunas = p ou n e linhas= q e m
    matriz = []
    print(f"Digite os elementos da matriz {nome} ({linhas}x{colunas}):")
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input(f"Digite o valor para a posição ({i+1}, {j+1}) da matriz {nome}: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def imprimir(matriz,nome,largura=4):
    print(f"\nMatriz {nome}:")
    # Percorre a matriz e imprime seus valores em forma de matriz
    for linha in matriz:
        # Formata cada elemento da linha para ter a largura especificada
        elementos_formatados = [f"{elemento:{largura}d}" for elemento in linha]
        # Junte os elementos formatados com um espaço e imprima a linha
        print(" ".join(elementos_formatados))

def multiplicar(A, B, m, n, q, p):
    # Verifique se `n` é igual a `q`, pois essa é a condição para multiplicação
    if n != q:
        print("As matrizes não podem ser multiplicadas porque o número de colunas de A não é igual ao número de linhas de B.")
        return None
    
    # Inicialize a matriz resultante com `m` linhas e `p` colunas
    C = [[0 for _ in range(p)] for _ in range(m)]
    
    # Realiza a multiplicação de matrizes
    for i in range(m):
        for j in range(p):
            soma = 0
            for k in range(n):
                soma += A[i][k] * B[k][j]
            C[i][j] = soma
            
    return C

def main():
    # Ler as dimensões das matrizes A e B
    m = int(input("Digite o número de linhas da matriz A(m): "))
    n = int(input("Digite o número de colunas da matriz A(n): "))
    q = int(input("Digite o número de linhas da matriz B(q): "))
    p = int(input("Digite o número de colunas da matriz B(p): "))

    # Ler as matrizes A e B
    matriz_A = ler_matriz(m, n, "A")
    matriz_B = ler_matriz(q, p, "B")

    # Multiplicar as matrizes A e B
    matriz_C = multiplicar(matriz_A, matriz_B, m, n, q, p)

    # Verifica se a matriz resultante é válida
    if matriz_C is not None:
        # Imprimir as matrizes A, B e a matriz resultante
        imprimir(matriz_A, "A")
        imprimir(matriz_B, "B")
        imprimir(matriz_C, "C")

# Chama a função principal para iniciar o programa
main()
