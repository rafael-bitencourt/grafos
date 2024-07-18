'''[Representação] (2,0pts) Crie um tipo estruturado de dados ou uma classe que represente um grafo não-dirigido
e ponderado G(V, E, w), no qual V é o conjunto de vértices, E é o conjunto de arestas e w : E → R é a função que
mapeia o peso de cada aresta {u, v} ∈ E'''

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = {}
        self.pesos = {}
    
    def qtdVertices(self):
        return len(self.vertices)
    
    def qtdArestas(self):
        return len(self.arestas)
    
    def grau(self, v):
        return len(self.vizinhos(v)) if v in self.vertices else 0
    
    def rotulo(self, v):
        return self.vertices[v] if v in self.vertices else None
    
    def vizinhos(self, v):
        return self.arestas.get(v, set())
    
    def haAresta(self, u, v):
        return (u in self.arestas and v in self.arestas[u]) or (v in self.arestas and u in self.arestas[v])
    
    def peso(self, u, v):
        return self.pesos.get((u, v), float('inf')) if self.haAresta(u, v) else float('inf')
    
    def ler(self, arquivo):
        with open(arquivo, 'r') as file:
            linhas = file.readlines()
        
        modo_vertices = False
        modo_arestas = False
        for linha in linhas:
            if linha == '\n':
                return
            linha = linha.strip()
            if "*vertices" in linha:
                modo_vertices = True
            elif "*edges" in linha:
                modo_vertices = False
                modo_arestas = True
            elif modo_vertices:
                _, rotulo = linha.split()
                self.vertices[_] = rotulo
            elif modo_arestas:
                u, v, peso = linha.split()
                self.adicionar_aresta(u, v, float(peso))
    
    def adicionar_aresta(self, u, v, peso):
        if u not in self.arestas:
            self.arestas[u] = set()
        if v not in self.arestas:
            self.arestas[v] = set()
        self.arestas[u].add(v)
        self.arestas[v].add(u)
        self.pesos[(u, v)] = peso
        self.pesos[(v, u)] = peso  # Garantindo a não-direcionalidade





