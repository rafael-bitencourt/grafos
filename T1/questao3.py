from questao1 import Grafo
class Grafo_ciclio_euleriano(Grafo):
    def __init__(self):
        super().__init__()
    
    def todos_vertices_conectados(self):
        # Começa a busca pelo primeiro vértice de grau não-zero
        start_vertex = next((v for v, vizinhos in self.arestas.items() if vizinhos), None)
        if not start_vertex:
            return False
        
        # Faz um DFS para verificar se todos os vértices de grau não-zero estão conectados
        visitados = set()
        stack = [start_vertex]
        while stack:
            v = stack.pop()
            if v not in visitados:
                visitados.add(v)
                stack.extend(self.arestas[v] - visitados)
        
        return all(v in visitados or not self.arestas[v] for v in self.vertices)

    def ciclo_euleriano(self):
        # Verifica se todos os vértices com grau não-zero são conectados e têm grau par
        if not self.todos_vertices_conectados():
            return (0, [])
        if any(len(vizinhos) % 2 != 0 for vizinhos in self.arestas.values()):
            return (0, [])
        
        # Se passar pelas verificações, executa o algoritmo para encontrar o ciclo euleriano
        ciclo = []
        u = next(iter(self.arestas))
        stack = [u]
        while stack:
            v = stack[-1]
            if self.arestas[v]:
                u = self.arestas[v].pop()
                self.arestas[u].remove(v)
                stack.append(u)
            else:
                ciclo.append(stack.pop())
        return (1, ciclo)

caminho_do_arquivo = 'grafo_entrada.txt'
grafo = Grafo_ciclio_euleriano()
grafo.ler(caminho_do_arquivo)

# Verifica a existência de um ciclo euleriano e o imprime
existe_ciclo, ciclo = grafo.ciclo_euleriano()
print(existe_ciclo)
if existe_ciclo:
    print(' -> '.join(map(str, ciclo)))
