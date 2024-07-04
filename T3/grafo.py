# Estrutura de dados para representar um grafo

class Grafo:
    def __init__(self, dirigido=False, ponderado=True):
        self.vertices = {}
        self.arestas = {}
        self.pesos = {}
        self.dirigido = dirigido
        self.ponderado = ponderado
    
    def qtdVertices(self):
        return len(self.vertices)
    
    def qtdArestas(self):
        if self.dirigido:
            return sum(len(vs) for vs in self.arestas.values())
        else:
            return sum(len(vs) for vs in self.arestas.values()) // 2
    
    def grau(self, v):
        if self.dirigido:
            return len(self.vizinhos(v))
        else:
            return len(self.vizinhos(v)) if v in self.vertices else 0
    
    def rotulo(self, v):
        return self.vertices.get(v, None)
    
    def vizinhos(self, v):
        return self.arestas.get(v, set())
    
    def haAresta(self, u, v):
        if self.dirigido:
            return v in self.arestas.get(u, set())
        else:
            return (u in self.arestas and v in self.arestas[u]) or (v in self.arestas and u in self.arestas[v])
    
    def peso(self, u, v):
        if self.ponderado:
            return self.pesos.get((u, v), float('inf')) if self.haAresta(u, v) else float('inf')
        else:
            return 1 if self.haAresta(u, v) else float('inf')
    
    def ler(self, arquivo):
        with open(arquivo, 'r') as file:
            linhas = file.readlines()
        
        modo_vertices = False
        modo_arestas = False
        for linha in linhas:
            linha = linha.strip()
            if linha == "":
                return
            if "*vertices" in linha:
                modo_vertices = True
            elif "*edges" in linha or "*arcs" in linha:
                modo_vertices = False
                modo_arestas = True
            elif modo_vertices:
                identificador, rotulo = linha.split(maxsplit=1)
                self.vertices[identificador] = rotulo
            elif modo_arestas:
                partes = linha.split()
                u, v = partes[:2]
                peso = float(partes[2]) if self.ponderado and len(partes) > 2 else 1
                self.adicionar_aresta(u, v, peso)
    
    def adicionar_aresta(self, u, v, peso=1):
        if u not in self.arestas:
            self.arestas[u] = set()
        self.arestas[u].add(v)
        if not self.dirigido:
            if v not in self.arestas:
                self.arestas[v] = set()
            self.arestas[v].add(u)
        if self.ponderado:
            self.pesos[(u, v)] = peso
            if not self.dirigido:
                self.pesos[(v, u)] = peso
