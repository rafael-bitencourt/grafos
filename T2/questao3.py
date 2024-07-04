'''3) [Kruskal ou Prim] (3,0pts) Crie um programa que recebe um grafo não-dirigido e ponderado como argumento.
      Ao final, o programa deverá determinar qual a árvore geradora mínima. O programa deverá imprimir o somatório
      das arestas na árvore na primeira linha e as arestas que pertencem a árvore geradora mínima na segunda linha'''

from grafo import Grafo
import sys

def kruskal(grafo):
    arestas = []
    for u in grafo.vertices:
        for v in grafo.vizinhos(u):
            if u < v:
                arestas.append((u, v, grafo.peso(u, v)))
    arestas.sort(key=lambda x: x[2])
    arvore = []
    pai = {u: u for u in grafo.vertices}
    for u, v, peso in arestas:
        if pai[u] != pai[v]:
            arvore.append((u, v))
            pai_v = pai[v]
            for w in grafo.vertices:
                if pai[w] == pai_v:
                    pai[w] = pai[u]
    return arvore

grafo = Grafo(dirigido=False, ponderado=True)

# Lê o grafo de um arquivo passado como argumento na linha de comando
if len(sys.argv) > 1:
    grafo.ler(sys.argv[1])

arvore = kruskal(grafo)
soma = 0
for u, v in arvore:
    soma += grafo.peso(u, v)

print(soma)
for u, v in arvore:
    print(f'({u}-{v})', end=" ")