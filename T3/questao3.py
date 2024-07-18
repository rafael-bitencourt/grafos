'''3. [Coloração de Vértices] (2,5pts) Crie um programa que recebe um grafo não-dirigido e não-ponderado como
   argumento. Ao final, informe a coloração mínima e qual número cromático foi utilizado em cada vértice. Use o
   algoritmo de Lawler para cumprir essa questão. Ao final, imprima na tela a quantidade de cores encontradas (na
   primeira linha) e qual é a cor correspondente a cada vértice (segunda linha).'''

from grafo import Grafo
from itertools import chain, combinations
import sys


def welsh_powell(nome_arquivo: str):
    G = Grafo(dirigido=False, ponderado=False)
    G.ler(nome_arquivo)
    
    # Obter os vértices e seus graus, e armazenar como tuplas (vértice, grau)
    vertices_com_graus = [(v, G.grau(v)) for v in G.vertices.keys()]
    # Ordenar os vértices pelo grau em ordem decrescente
    vertices_com_graus.sort(key=lambda x: x[1], reverse=True)

    # Inicializar a coloração
    coloracao = {v: None for v, _ in vertices_com_graus}
    
    # Iniciar a coloração
    cor_atual = 0
    for v, _ in vertices_com_graus:
        if coloracao[v] is None:  # Se o vértice ainda não foi colorido
            cor_atual += 1
            coloracao[v] = cor_atual
            # Tentar colorir os vértices não adjacentes com a mesma cor
            for w, _ in vertices_com_graus:
                if w != v and coloracao[w] is None:
                    # Verificar se todos os vizinhos de w têm cores diferentes de cor_atual
                    if all(coloracao.get(n) != cor_atual for n in G.vizinhos(w)):
                        coloracao[w] = cor_atual

    return cor_atual, coloracao

def imprimir_resultado(nome_arquivo: str):
    numero_cores, vertices_coloridos = welsh_powell(nome_arquivo)
    print(f"Número de Cores: {numero_cores}")
    print()
    for v, cor in vertices_coloridos.items():
        print(f"O vértice {v} tem cor {cor}")

# printa_resultado('instances/coloracao/corWiki.net')


#printa_resultado(sys.argv[1])
arquivo = sys.argv[1]
imprimir_resultado(f'instances/coloracao/{arquivo}')
