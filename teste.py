from meu_grafo_matriz_adjacencia_nao_dir import MeuGrafo

g_p2 = MeuGrafo(['J', 'C'])
g_p2.adicionaAresta('a1', 'J', 'C')
# g_p2.adicionaAresta('a2', 'C', 'E')
# # g_p.adicionaAresta('a3', 'C', 'E')
# g_p.adicionaAresta('a4', 'P', 'C')
# g_p.adicionaAresta('a5', 'P', 'C')
# g_p.adicionaAresta('a6', 'T', 'C')
# g_p.adicionaAresta('a7', 'M', 'C')
# g_p.adicionaAresta('a8', 'M', 'T')
# g_p.adicionaAresta('a9', 'T', 'Z')

g_p3 = MeuGrafo(['J', 'C', 'E'])
g_p3.adicionaAresta('a1', 'J', 'C')
g_p3.adicionaAresta('a2', 'C', 'E')

g_p2.conexo()

g_p3.conexo()
