# variaveis
phoneBook = {}
n = 0

# quantidade de itens
N = int(input())

# nome e telefone
for _ in range(N):
    nome, telefone = map(str, input().split())
    phoneBook[nome.lower()] = int(telefone)

# nome a ser procurado
while n < N:

    pesquisa = str(input())

    if pesquisa in phoneBook.keys():
        print('{}={} '.format(pesquisa, phoneBook.get(pesquisa)))
    else:
        print('Not found')

    n += 1