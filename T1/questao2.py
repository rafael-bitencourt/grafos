''' Crie um programa que receba um arquivo de grafo e o índice do vértice s como argumentos. O
programa deve fazer uma busca em largura a partir de s e deverá imprimir a saída na tela, onde cada linha deverá
conter o nível seguido de “:” e a listagem de vértices encontrados naquele nível. '''

from questao1 import Grafo

def buscaLargura(grafo, s):
    vertices_por_nivel = {}
    visitados = {s}
    fila = [(s, 0)]
    nivel = 0
    while fila:
        v, nivel = fila.pop(0)
        if nivel not in vertices_por_nivel:
            vertices_por_nivel[nivel] = []
        vertices_por_nivel[nivel].append(v)
        for u in grafo.vizinhos(v):
            if u not in visitados:
                visitados.add(u)
                fila.append((u, nivel + 1))
    for nivel in vertices_por_nivel:
        print(nivel, ":", vertices_por_nivel[nivel])

caminho = 'grafo_entrada.txt'
grafo = Grafo()
grafo.ler(caminho)
s = '1'
buscaLargura(grafo, s)

