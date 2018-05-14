# quantidade de entrada
number = int(input())

# variavel
lista = []
listaEven = []
listaOdd = []

# entradas
for _ in range(number):
    lista.append(str(input()))

# percorrer lista de palavras
for i in range(len(lista)):
    # percorrer palavra
    for j in range(len(lista[i])):
        # if even
        if j % 2 == 0:
            listaEven.append(lista[i][j])
        # if odd
        else:
            listaOdd.append(lista[i][j])
    listaEven.append(' ')

    # resultados
    even = ''.join(listaEven)
    odd = ''.join(listaOdd)
    result = even + odd

    # apagando listas
    listaEven = []
    listaOdd = []

    # mostrar resultado
    print(result)
