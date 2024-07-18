from questao1 import Grafo

class Grafo_FloydWarshall(Grafo):
    def __init__(self):
        super().__init__()
    
    def floyd_warshall(self):
        # Inicializa a matriz de distâncias
        dist = {v: {u: float('inf') for u in self.vertices} for v in self.vertices}
        for v in self.vertices:
            dist[v][v] = 0
        for u in self.arestas:
            for v in self.arestas[u]:
                dist[u][v] = self.peso(u, v)
        
        # Algoritmo de Floyd-Warshall
        for k in self.vertices:
            for i in self.vertices:
                for j in self.vertices:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist

    def imprimir_distancias(self):
        distancias = self.floyd_warshall()
        for i in sorted(self.vertices, key=int):  # Ordena pelo índice, assegurando ordem crescente
            linha = ""
            for j in sorted(self.vertices, key=int):
                distancia = distancias[i][j]
                linha += f" {distancia if distancia != float('inf') else '∞'},"
            print(linha.rstrip(','))

grafo = Grafo_FloydWarshall()
grafo.ler("grafo_entrada.txt")
grafo.imprimir_distancias()

