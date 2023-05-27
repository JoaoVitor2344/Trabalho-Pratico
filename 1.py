def busca_em_profunidade(grafo, inicio, fim):
    pilha = []
    visitados = set()
    pilha.append(inicio)
    while pilha:
        vertice = pilha.pop()
        if vertice == fim:
            return True
        if vertice not in visitados:
            visitados.add(vertice)
            pilha.extend(grafo[vertice] - visitados)
    return False

# Path: 2.py
def busca_em_largura(grafo, inicio, fim):
    fila = []
    visitados = set()
    fila.append(inicio)
    while fila:
        vertice = fila.pop(0)
        if vertice == fim:
            return True
        if vertice not in visitados:
            visitados.add(vertice)
            fila.extend(grafo[vertice] - visitados)
    return False

def busca_com_djikstra(grafo, inicio, fim):
    fila = []
    visitados = set()
    fila.append(inicio)
    while fila:
        vertice = fila.pop(0)
        if vertice == fim:
            return True
        if vertice not in visitados:
            visitados.add(vertice)
            fila.extend(grafo[vertice] - visitados)
    return False

# Função que calcula a diferença de velocidade entre a busca em profundidade e a busca em largura
def diferenca_velocidade():
    import timeit
    setup = '''
from __main__ import busca_em_profunidade, busca_em_largura, grafo
    '''
    print(timeit.timeit('busca_em_profunidade(grafo, (1, 1), (8, 8))', setup=setup, number=10000))
    print(timeit.timeit('busca_em_largura(grafo, (1, 1), (8, 8))', setup=setup, number=10000))

if __name__ == '__main__':
    labirinto = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 0
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 1
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1], # 2
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1], # 3
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1], # 4
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 1], # 5
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1], # 6
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 1], # 7
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 1], # 8
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 9
    ]

    grafo = {}
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if labirinto[i][j] == 0:
                grafo[(i, j)] = set()
                if i > 0 and labirinto[i - 1][j] == 0:
                    grafo[(i, j)].add((i - 1, j))
                if i < len(labirinto) - 1 and labirinto[i + 1][j] == 0:
                    grafo[(i, j)].add((i + 1, j))
                if j > 0 and labirinto[i][j - 1] == 0:
                    grafo[(i, j)].add((i, j - 1))
                if j < len(labirinto[i]) - 1 and labirinto[i][j + 1] == 0:
                    grafo[(i, j)].add((i, j + 1))

    diferenca_velocidade()
