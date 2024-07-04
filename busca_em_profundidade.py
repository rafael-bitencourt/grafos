import math

grafo = {
    'a': ['b', 'c', 'd'],
    'b': ['c', 'e'],
    'c': ['a', 'd', 'f'],
    'd': ['b', 'e'],
    'e': ['a', 'f'],
    'f': ['b', 'c']
}


def dfs(grafo, origem):
    visitado = {v: False for v in grafo}  # Cv
    tempo_visita = {v: float('inf') for v in grafo}  # Tv
    antecessor = {v: None for v in grafo}  # Av
    
    visitado[origem] = True
    tempo = 0
    
    pilha = [origem]  # Utilizamos uma lista como pilha
    
    while pilha:
        tempo += 1
        u = pilha.pop()
        tempo_visita[u] = tempo
        
        for v in grafo[u]:
            if not visitado[v]:
                visitado[v] = True
                antecessor[v] = u
                pilha.append(v)
    
    return visitado, tempo_visita, antecessor


origem = 'a'
visitado, tempo_visita, antecessor = dfs(grafo, origem)
print("Visitado:", visitado)
print("Tempo de visita:", tempo_visita)
print("Antecessor:", antecessor)