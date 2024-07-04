''' 1) [Componentes Fortemente Conexas] (3,0pts) Crie um programa que receba um grafo dirigido e não-ponderado
       como argumento. Ao final, imprima na tela as componentes fortemente conexas desse grafo.'''

from grafo import Grafo
import sys

def componentes_fortemente_conexas(grafo):
    def visitar(v, tempo, pilha, visitados, componentes):
        visitados.add(v)
        tempo += 1
        pilha.append(v)
        tempo_descoberta[v] = tempo
        tempo_finalizacao[v] = tempo
        for u in grafo.vizinhos(v):
            if u not in visitados:
                tempo = visitar(u, tempo, pilha, visitados, componentes)
            tempo_finalizacao[v] = min(tempo_finalizacao[v], tempo_finalizacao[u])
        if tempo_descoberta[v] == tempo_finalizacao[v]:
            componente = set()
            while True:
                u = pilha.pop()
                componente.add(u)
                if u == v:
                    break
            componentes.append(componente)
        return tempo

    visitados = set()
    tempo_descoberta = {}
    tempo_finalizacao = {}
    pilha = []
    componentes = []
    tempo = 0
    for v in grafo.vertices:
        if v not in visitados:
            tempo = visitar(v, tempo, pilha, visitados, componentes)
    return componentes


grafo = Grafo(dirigido=True, ponderado=False)

# Lê o grafo de um arquivo passado como argumento na linha de comando
if len(sys.argv) > 1:
    grafo.ler(sys.argv[1])

componentes = componentes_fortemente_conexas(grafo)
for componente in componentes:
    for v in componente:
        print(v, end=" ")
    print()
    
