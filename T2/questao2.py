'''2) [Ordenação Topológica] (3,0pts) Crie um programa que receba um arquivo de grafo dirigido não-ponderado com
      vértices rotulados como argumento. O programa deve fazer executar uma Ordenação Topológica'''


from grafo import Grafo
import sys

def ordenacao_topologica(grafo):
    grau = {}
    for vertice in grafo.vertices:
        grau[vertice] = 0
    for vertice in grafo.vertices:
        for adjacente in grafo.vizinhos(vertice):
            grau[adjacente] += 1
    fila = []
    for vertice in grafo.vertices:
        if grau[vertice] == 0:
            fila.append(vertice)
    ordenacao = []
    while fila:
        vertice = fila.pop(0)
        ordenacao.append(vertice)
        for adjacente in grafo.vizinhos(vertice):
            grau[adjacente] -= 1
            if grau[adjacente] == 0:
                fila.append(adjacente)
    return ordenacao


grafo = Grafo(dirigido=True, ponderado=False)

# Lê o grafo de um arquivo passado como argumento na linha de comando
if len(sys.argv) > 1:
    grafo.ler(sys.argv[1])

ordenacao = ordenacao_topologica(grafo)
for vertice in ordenacao:
    if vertice != ordenacao[-1]:
        print(grafo.vertices[vertice], end="->")
    else:
        print(grafo.vertices[vertice])