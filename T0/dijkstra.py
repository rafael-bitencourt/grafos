import heapq  

def dijkstra(grafo, inicio):
    # Inicializa as distâncias com infinito e a distância da origem como 0
    distancias = {vertice: float('infinity') for vertice in grafo}
    distancias[inicio] = 0

    # Prioridade dos vértices ainda não visitados
    fila_prioridade = [(0, inicio)]

    while fila_prioridade:
        # Seleciona o vértice com a menor distância
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        # Processa cada adjacente apenas uma vez
        for vizinho, peso in grafo[vertice_atual].items():
            nova_distancia = distancia_atual + peso
            
            # Só atualiza se encontrou um caminho mais curto
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))
    
    return distancias


# Exemplo de uso
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(dijkstra(grafo, 'A'))
