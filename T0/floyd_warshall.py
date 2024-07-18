def floyd_warshall(n, edges):
    # Inicia a matriz de distâncias com infinito e as diagonais com zero
    dist = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]
    
    # Aplica os pesos iniciais do grafo
    for u, v, w in edges:
        dist[u][v] = w

    # Atualiza as distâncias usando cada vértice como intermediário
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Minimiza a distância com o vértice intermediário k
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Exibir a matriz após cada atualização
        print(f"Matriz D({k}):")
        for row in dist:
            print(row)
    
    return dist

# Exemplo de uso
edges = [(0, 1, 1), (1, 2, 2), (2, 0, 4)]
n = 3
print(floyd_warshall(n, edges))
