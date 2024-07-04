''' Lista de adjacência ''' 
grafo = { 'a': {'b': 1, 'c': 2}, 'b': {'c': 3}, 'c': {'a': 4} }

print('lista de adjacência')
# criar arranjo Adj[|V|]
Adj = {}

for u in grafo:
    Adj[u] = []
    for v in grafo[u]:
        Adj[u].append((v, grafo[u][v]))
print(Adj)


''' Matriz de adjacência '''
print('\nmatriz de adjacência')
# criar matriz Adj[|V|][|V|]
A = [[0 for i in range(3)] for j in range(3)]
for u in grafo:
    for v in grafo[u]:
        A[ord(u)-97][ord(v)-97] = grafo[u][v]

for i in range(3):
    for j in range(3):
        print(A[i][j], end=' ')
    print()

