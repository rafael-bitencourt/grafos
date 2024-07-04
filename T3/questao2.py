'''2. [Hopcroft-Karp] (2,5pts) Crie um programa que receba um arquivo de grafo bipartido, não-dirigido, não-ponderado
   e informe qual o valor do emparelhamento máximo e quais arestas pertencem a ele. Utilize o algoritmo de Hopcroft-
   Karp. Ao final, imprima na tela a quantidade de emparelhamentos encontrados (na primeira linha) e quais são as
   arestas correspondentes (na segunda linha)'''

from queue import Queue
from grafo import Grafo
import sys

INF = 2147483647
NIL = 0

def bfs(grafo, pairU, pairV, dist):
    Q = Queue()
    for u in range(1, grafo.m + 1):
        if pairU[u] == NIL:
            dist[u] = 0
            Q.put(u)
        else:
            dist[u] = INF
    dist[NIL] = INF
    while not Q.empty():
        u = Q.get()
        if dist[u] < dist[NIL]:
            for v in grafo.adj[u]:
                if dist[pairV[v]] == INF:
                    dist[pairV[v]] = dist[u] + 1
                    Q.put(pairV[v])
    return dist[NIL] != INF

def dfs(grafo, u, pairU, pairV, dist):
    if u != NIL:
        for v in grafo.adj[u]:
            if dist[pairV[v]] == dist[u] + 1:
                if dfs(grafo, pairV[v], pairU, pairV, dist):
                    pairV[v] = u
                    pairU[u] = v
                    return True
        dist[u] = INF
        return False
    return True

def hopcroft_karp(grafo):
    pairU = [NIL] * (grafo.m + 1)
    pairV = [NIL] * (grafo.n + 1)
    dist = [0] * (grafo.m + 1)
    matching = 0
    matching_edges = []
    while bfs(grafo, pairU, pairV, dist):
        for u in range(1, grafo.m + 1):
            if pairU[u] == NIL and dfs(grafo, u, pairU, pairV, dist):
                matching += 1
                matching_edges.append((u, pairU[u]))
    return matching, matching_edges

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <arquivo_do_grafo>")
        sys.exit(1)
    g = Grafo(dirigido=False, ponderado=False)
    nome_do_arquivo = sys.argv[1]
    g.ler(nome_do_arquivo)
    matching, matching_edges = hopcroft_karp(g)
    print(matching)
    for u, v in matching_edges:
        print(f"({u}, {v})", end=" ")
    print()