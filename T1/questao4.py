import heapq  
from questao1 import Grafo

class Grafo_Dijkstra(Grafo):
    def __init__(self):
        super().__init__()

    def dijkstra(self, s):
        dist = {v: float('inf') for v in self.vertices}
        prev = {v: None for v in self.vertices}
        dist[s] = 0
        queue = [(0, s)]

        while queue:
            d, u = heapq.heappop(queue)
            if d > dist[u]:
                continue
            for v in self.vizinhos(u):
                alt = d + self.peso(u, v)
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(queue, (alt, v))
        return dist, prev

    def reconstruir_caminho(self, start, end, prev):
        caminho = []
        passo = end
        while passo is not None:
            caminho.append(passo)
            passo = prev[passo]
        caminho.reverse()

        return caminho if caminho[0] == start else []

    def imprimir_caminhos(self, s):
        distancias, predecessores = self.dijkstra(s)
        for v in self.vertices:
            if v == s:
                continue
            caminho = self.reconstruir_caminho(s, v, predecessores)
            caminho_descrito = ' -> '.join([self.rotulo(vert) for vert in caminho]) if caminho else "Sem caminho possível"
            print(f"{self.rotulo(v)}: {caminho_descrito} d={distancias[v] if distancias[v] != float('inf') else 'Infinito'}")

grafo = Grafo_Dijkstra()
grafo.ler("grafo_entrada.txt") 
s = '1'  
grafo.imprimir_caminhos(s)
