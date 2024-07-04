import math

grafo = {
    'a': ['b', 'c', 'd'],
    'b': ['c', 'e'],
    'c': ['a', 'd', 'f'],
    'd': ['b', 'e'],
    'e': ['a', 'f'],
    'f': ['b', 'c']
}

# Busca em largura

from collections import deque

def bfs(grafo, origem):
    visitado = {v: False for v in grafo}  # Cv
    distancia = {v: float('inf') for v in grafo}  # Dv
    antecessor = {v: None for v in grafo}  # Av
    
    visitado[origem] = True
    distancia[origem] = 0
    
    fila = deque([origem]) # Cria a fila com a origem
    
    while fila:
        u = fila.popleft() # Retira primeiro elemento da fila
        for v in grafo[u]:
            if not visitado[v]:
                visitado[v] = True
                distancia[v] = distancia[u] + 1
                antecessor[v] = u
                fila.append(v)
    
    return visitado, distancia, antecessor

# Exemplo de uso:
origem = 'a'
visitado, distancia, antecessor = bfs(grafo, origem)
print("Visitado:", visitado)
print("Distância:", distancia)
print("Antecessor:", antecessor)


