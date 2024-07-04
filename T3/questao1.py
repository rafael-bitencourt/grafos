'''1. [Edmonds-Karp] (2,5pts) Crie um programa que receba um grafo dirigido e ponderado como argumento. Ao final,
      imprima na tela o valor do fluxo máximo resultante da execução do algoritmo de Edmonds-Karp'''

from collections import deque
from grafo import Grafo
import sys

def edmonds_karp(grafo):

    fonte = list(grafo.vertices.keys())[0]
    sorvedouro = list(grafo.vertices.keys())[len(grafo.vertices) - 1]


    antecessor = {v: None for v in grafo.vertices}
    fluxo_maximo = 0

    while bfs(grafo, fonte, sorvedouro, antecessor):
        
        caminho_aumentante = float('inf')
        s = sorvedouro

        while s != fonte:
            caminho_aumentante = min(caminho_aumentante, grafo.peso(antecessor[s], s))
            s = antecessor[s]

        fluxo_maximo += caminho_aumentante
        v = sorvedouro

        while v != fonte:
            u = antecessor[v]
            grafo.adicionar_aresta(u, v, (grafo.peso(u, v) - caminho_aumentante))
            grafo.adicionar_aresta(v, u, (grafo.peso(v, u) + caminho_aumentante))
            v = antecessor[v]

    return fluxo_maximo


def bfs(grafo, s, t, antecessor):
        
        visitado = {v: False for v in grafo.vertices}
        fila = []
        fila.append(s)
        visitado[s] = True

        while fila:
            u = fila.pop(0)

            for v in grafo.vizinhos(u):
                if not visitado[v] and grafo.peso(u, v) > 0:
                    fila.append(v)
                    visitado[v] = True
                    antecessor[v] = u

        return visitado[t]


grafo = Grafo(dirigido=True, ponderado=True)

if len(sys.argv) > 1:
    grafo.ler(f'instances/fluxo_maximo/{sys.argv[1]}')

print(edmonds_karp(grafo))