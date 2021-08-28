# from meu_grafo import MeuGrafo
# from meu_grafo_matriz_adjacencia_nao_dir import MeuGrafo
from meu_grafo_matriz_adjacencia_dir import MeuGrafo

g_p = MeuGrafo(['a', 'b', 'c', 'd'])
g_p.adicionaAresta('a1', 'a', 'b')
g_p.adicionaAresta('a2', 'a', 'c')
g_p.adicionaAresta('a3', 'b', 'c')
g_p.adicionaAresta('a4', 'c', 'a')
g_p.adicionaAresta('a5', 'c', 'd')

teste = MeuGrafo(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
teste.adicionaAresta('a1', 'a', 'b')
teste.adicionaAresta('a2', 'a', 'd')
teste.adicionaAresta('a3', 'b', 'c')
teste.adicionaAresta('a4', 'c', 'd')
teste.adicionaAresta('a5', 'd', 'e')
teste.adicionaAresta('a6', 'e', 'f')
teste.adicionaAresta('a7', 'e', 'h')
teste.adicionaAresta('a8', 'f', 'g')
teste.adicionaAresta('a9', 'g', 'h')

pares = MeuGrafo(['a', 'b', 'c', 'd', 'e', 'f'])
pares.adicionaAresta('a1', 'a', 'b')
pares.adicionaAresta('a2', 'f', 'a')
pares.adicionaAresta('a3', 'b', 'c')
pares.adicionaAresta('a4', 'c', 'd')
pares.adicionaAresta('a5', 'd', 'e')
pares.adicionaAresta('a6', 'e', 'f')

print(pares.existe_caminho('a', 'a'))
