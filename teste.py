from meu_grafo_matriz_adjacencia_nao_dir import MeuGrafo

g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p.adicionaAresta('a1', 'J', 'C')
g_p.adicionaAresta('a2', 'C', 'E')
g_p.adicionaAresta('a3', 'C', 'E')
g_p.adicionaAresta('a4', 'P', 'C')
g_p.adicionaAresta('a5', 'P', 'C')
g_p.adicionaAresta('a6', 'T', 'C')
g_p.adicionaAresta('a7', 'M', 'C')
g_p.adicionaAresta('a8', 'M', 'T')
g_p.adicionaAresta('a9', 'T', 'Z')

print(g_p.conexo())

g_d = MeuGrafo(['A', 'B', 'C', 'D'])
g_d.adicionaAresta('asd', 'A', 'B')

outro = MeuGrafo(['1', '2', '3', '4', '5', '6'])
outro.adicionaAresta('a1', '1', '2')
outro.adicionaAresta('a2', '2', '3')
outro.adicionaAresta('a3', '3', '4')
outro.adicionaAresta('a4', '4', '5')

print(g_d.conexo())
print(outro.conexo())
