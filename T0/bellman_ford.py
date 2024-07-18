# Bellman-Ford: algoritmo de caminhos mínimos para grafos com pesos negativos e ciclos

def bellman_ford(G, s):
    # Inicialização das estruturas de dados
    D = {v: float('inf') for v in G}
    A = {v: None for v in G}
    D[s] = 0
    
    # Iterações
    for _ in range(len(G) - 1):
        for u in G:
            for v in G[u]:
                # Relaxamento
                if D[v] > D[u] + G[u][v]:
                    D[v] = D[u] + G[u][v]
                    A[v] = u
    
    # Verificação de ciclos negativos
    for u in G:
        for v in G[u]:
            if D[v] > D[u] + G[u][v]:
                return False, None, None
    
    # Retorno dos resultados
    return True, D, A

# Exemplo de uso:
grafo = {
    's': {'a': 4, 'b': 3},
    'a': {'c': 2},
    'b': {'a': 1, 'c': -5},  # Aresta com peso negativo
    'c': {'t': 3},
    't': {}
}
origem = 's'
resultado, D, A = bellman_ford(grafo, origem)
print("Ciclo de peso negativo encontrado:", not resultado)
print("Estimativa de caminho mínimo:", D)
print("Vértice anterior:", A)




