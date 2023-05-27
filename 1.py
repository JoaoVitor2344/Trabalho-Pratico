# Função que retorna os vizinhos de uma posição
def vizinhos(labirinto, posicao) :
    linhas = len(labirinto)
    colunas = len(labirinto[0])
    vizinhos = []

    if posicao[0] > 0 and labirinto[posicao[0] - 1][posicao[1]] != 1 :
        vizinhos.append((posicao[0] - 1, posicao[1]))
    if posicao[0] < linhas - 1 and labirinto[posicao[0] + 1][posicao[1]] != 1 :
        vizinhos.append((posicao[0] + 1, posicao[1]))
    if posicao[1] > 0 and labirinto[posicao[0]][posicao[1] - 1] != 1 :
        vizinhos.append((posicao[0], posicao[1] - 1))
    if posicao[1] < colunas - 1 and labirinto[posicao[0]][posicao[1] + 1] != 1 :
        vizinhos.append((posicao[0], posicao[1] + 1))
    
    return vizinhos

# Função que retorna o caminho mais curto entre dois pontos
def caminho_mais_curto(labirinto, partida, chegada) :
    linhas = len(labirinto)
    colunas = len(labirinto[0])

    # Função recursiva que explora os caminhos
    def explora_caminho(labirinto, posicao, chegada, caminho) :
        if posicao == chegada :
            return caminho + [posicao]
        else :
            caminho.append(posicao)

            for vizinho in vizinhos(labirinto, posicao) :
                if vizinho not in caminho :
                    caminho_encontrado = explora_caminho(labirinto, vizinho, chegada, caminho)
                    if caminho_encontrado != None :
                        return caminho_encontrado
            caminho.pop()
            return "Não há caminho possível"
        
    return explora_caminho(labirinto, partida, chegada, [])

if __name__ == '__main__':
    # Labirinto 0 = caminho livre 1 = parede
    labirinto = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0 ,1, 1, 1, 1, 1, 0],
        [0, 0, 0 ,1, 0, 0, 0, 0, 0],
        [0, 1, 0 ,1, 0, 1, 1, 1, 1],
        [0, 1, 0 ,1, 0, 0, 0, 0, 0],
        [0, 1, 0 ,1, 0, 1, 1, 1, 0],
        [0, 1, 0 ,1, 0, 0, 0, 1, 0],
        [0, 1, 0 ,1, 1, 1, 0, 1, 0],
        [0, 1, 0 ,0, 0, 0, 0, 1, 0],
        [0, 1, 1 ,1, 1, 1, 1, 1, 0],
        [0, 0, 0 ,0, 0, 0, 0, 0, 0]
    ]

    # Exemplo de partida e chegada
    partida = (0, 0)
    chegada = (10, 8)

    # Chamada da função
    caminho = caminho_mais_curto(labirinto, partida, chegada)

    # Imprime o caminho
    print(caminho)