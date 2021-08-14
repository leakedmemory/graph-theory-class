from meu_grafo_matriz_adjacencia_nao_dir import MeuGrafo

g_p = MeuGrafo(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
g_p.adicionaAresta('a1', 'a', 'b')
g_p.adicionaAresta('a2', 'a', 'c')
g_p.adicionaAresta('a3', 'a', 'd')
g_p.adicionaAresta('a4', 'a', 'f')
g_p.adicionaAresta('a5', 'b', 'c')
g_p.adicionaAresta('a6', 'b', 'g')
g_p.adicionaAresta('a7', 'b', 'e')
g_p.adicionaAresta('a8', 'e', 'f')
g_p.adicionaAresta('a9', 'f', 'g')

print(g_p)
g_p.remove_aresta('a1')
print(g_p)
