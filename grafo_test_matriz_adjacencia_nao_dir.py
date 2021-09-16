import unittest

import bibgrafo.grafo_exceptions

from meu_grafo_matriz_adjacencia_nao_dir import MeuGrafo


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1', 'J', 'C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        self.outro = MeuGrafo(['1', '2', '3', '4', '5', '6'])
        self.outro.adicionaAresta('a1', '1', '2')
        self.outro.adicionaAresta('a2', '2', '3')
        self.outro.adicionaAresta('a3', '3', '4')
        self.outro.adicionaAresta('a4', '4', '5')

        # Grafos pai para exemplo teste
        self.g_pequeno = MeuGrafo(['1', '2', '3', '4', '5'])
        self.g_pequeno.adicionaAresta('a1', '1', '2')
        self.g_pequeno.adicionaAresta('a2', '1', '3')
        self.g_pequeno.adicionaAresta('a3', '2', '4')
        self.g_pequeno.adicionaAresta('a4', '2', '5')

        self.g_medio = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.g_medio.adicionaAresta('a1', '1', '2')
        self.g_medio.adicionaAresta('a2', '1', '3')
        self.g_medio.adicionaAresta('a3', '3', '4')
        self.g_medio.adicionaAresta('a4', '4', '5')
        self.g_medio.adicionaAresta('a5', '5', '6')
        self.g_medio.adicionaAresta('a6', '2', '6')
        self.g_medio.adicionaAresta('a7', '2', '7')
        self.g_medio.adicionaAresta('a8', '6', '7')
        self.g_medio.adicionaAresta('a9', '7', '8')
        self.g_medio.adicionaAresta('a10', '8', '9')
        self.g_medio.adicionaAresta('a11', '8', '10')
        self.g_medio.adicionaAresta('a12', '9', '10')

        self.g_grande = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
             '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
             '24', '25', '26', '27', '28', '29', '30'])
        self.g_grande.adicionaAresta('a1', '1', '2')
        self.g_grande.adicionaAresta('a2', '2', '3')
        self.g_grande.adicionaAresta('a3', '1', '4')
        self.g_grande.adicionaAresta('a4', '3', '4')
        self.g_grande.adicionaAresta('a5', '3', '5')
        self.g_grande.adicionaAresta('a6', '3', '8')
        self.g_grande.adicionaAresta('a7', '8', '12')
        self.g_grande.adicionaAresta('a8', '8', '9')
        self.g_grande.adicionaAresta('a9', '8', '11')
        self.g_grande.adicionaAresta('a10', '12', '13')
        self.g_grande.adicionaAresta('a11', '13', '14')
        self.g_grande.adicionaAresta('a12', '14', '16')
        self.g_grande.adicionaAresta('a13', '14', '15')
        self.g_grande.adicionaAresta('a14', '4', '6')
        self.g_grande.adicionaAresta('a15', '6', '30')
        self.g_grande.adicionaAresta('a16', '30', '29')
        self.g_grande.adicionaAresta('a17', '29', '28')
        self.g_grande.adicionaAresta('a18', '28', '25')
        self.g_grande.adicionaAresta('a19', '28', '27')
        self.g_grande.adicionaAresta('a20', '27', '26')
        self.g_grande.adicionaAresta('a21', '26', '25')
        self.g_grande.adicionaAresta('a22', '25', '23')
        self.g_grande.adicionaAresta('a23', '23', '24')
        self.g_grande.adicionaAresta('a24', '23', '7')
        self.g_grande.adicionaAresta('a25', '7', '5')
        self.g_grande.adicionaAresta('a26', '23', '22')
        self.g_grande.adicionaAresta('a27', '22', '21')
        self.g_grande.adicionaAresta('a28', '21', '20')
        self.g_grande.adicionaAresta('a29', '20', '19')
        self.g_grande.adicionaAresta('a30', '19', '17')
        self.g_grande.adicionaAresta('a31', '17', '16')
        self.g_grande.adicionaAresta('a32', '17', '18')
        self.g_grande.adicionaAresta('a33', '18', '19')
        self.g_grande.adicionaAresta('a34', '20', '10')
        self.g_grande.adicionaAresta('a35', '10', '9')
        self.g_grande.adicionaAresta('a36', '10', '11')

        # Grafos para teste de DFS
        self.g_medio_dfs1 = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.g_medio_dfs1.adicionaAresta('a1', '1', '2')
        self.g_medio_dfs1.adicionaAresta('a3', '3', '4')
        self.g_medio_dfs1.adicionaAresta('a4', '4', '5')
        self.g_medio_dfs1.adicionaAresta('a5', '5', '6')
        self.g_medio_dfs1.adicionaAresta('a6', '2', '6')
        self.g_medio_dfs1.adicionaAresta('a8', '6', '7')
        self.g_medio_dfs1.adicionaAresta('a9', '7', '8')
        self.g_medio_dfs1.adicionaAresta('a10', '8', '9')
        self.g_medio_dfs1.adicionaAresta('a12', '9', '10')

        self.g_medio_dfs5 = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.g_medio_dfs5.adicionaAresta('a1', '1', '2')
        self.g_medio_dfs5.adicionaAresta('a2', '1', '3')
        self.g_medio_dfs5.adicionaAresta('a3', '3', '4')
        self.g_medio_dfs5.adicionaAresta('a4', '4', '5')
        self.g_medio_dfs5.adicionaAresta('a6', '2', '6')
        self.g_medio_dfs5.adicionaAresta('a8', '6', '7')
        self.g_medio_dfs5.adicionaAresta('a9', '7', '8')
        self.g_medio_dfs5.adicionaAresta('a10', '8', '9')
        self.g_medio_dfs5.adicionaAresta('a12', '9', '10')

        self.g_medio_dfs7 = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.g_medio_dfs7.adicionaAresta('a1', '1', '2')
        self.g_medio_dfs7.adicionaAresta('a2', '1', '3')
        self.g_medio_dfs7.adicionaAresta('a3', '3', '4')
        self.g_medio_dfs7.adicionaAresta('a4', '4', '5')
        self.g_medio_dfs7.adicionaAresta('a5', '5', '6')
        self.g_medio_dfs7.adicionaAresta('a7', '2', '7')
        self.g_medio_dfs7.adicionaAresta('a9', '7', '8')
        self.g_medio_dfs7.adicionaAresta('a10', '8', '9')
        self.g_medio_dfs7.adicionaAresta('a12', '9', '10')

        self.g_medio_dfs9 = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.g_medio_dfs9.adicionaAresta('a1', '1', '2')
        self.g_medio_dfs9.adicionaAresta('a2', '1', '3')
        self.g_medio_dfs9.adicionaAresta('a3', '3', '4')
        self.g_medio_dfs9.adicionaAresta('a4', '4', '5')
        self.g_medio_dfs9.adicionaAresta('a5', '5', '6')
        self.g_medio_dfs9.adicionaAresta('a7', '2', '7')
        self.g_medio_dfs9.adicionaAresta('a9', '7', '8')
        self.g_medio_dfs9.adicionaAresta('a10', '8', '9')
        self.g_medio_dfs9.adicionaAresta('a11', '8', '10')

        self.g_grande_dfs1 = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
             '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
             '24', '25', '26', '27', '28', '29', '30'])
        self.g_grande_dfs1.adicionaAresta('a1', '1', '2')
        self.g_grande_dfs1.adicionaAresta('a2', '2', '3')
        self.g_grande_dfs1.adicionaAresta('a4', '3', '4')
        self.g_grande_dfs1.adicionaAresta('a7', '8', '12')
        self.g_grande_dfs1.adicionaAresta('a8', '8', '9')
        self.g_grande_dfs1.adicionaAresta('a10', '12', '13')
        self.g_grande_dfs1.adicionaAresta('a11', '13', '14')
        self.g_grande_dfs1.adicionaAresta('a12', '14', '16')
        self.g_grande_dfs1.adicionaAresta('a13', '14', '15')
        self.g_grande_dfs1.adicionaAresta('a14', '4', '6')
        self.g_grande_dfs1.adicionaAresta('a15', '6', '30')
        self.g_grande_dfs1.adicionaAresta('a16', '30', '29')
        self.g_grande_dfs1.adicionaAresta('a17', '29', '28')
        self.g_grande_dfs1.adicionaAresta('a18', '28', '25')
        self.g_grande_dfs1.adicionaAresta('a20', '27', '26')
        self.g_grande_dfs1.adicionaAresta('a21', '26', '25')
        self.g_grande_dfs1.adicionaAresta('a22', '25', '23')
        self.g_grande_dfs1.adicionaAresta('a23', '23', '24')
        self.g_grande_dfs1.adicionaAresta('a24', '23', '7')
        self.g_grande_dfs1.adicionaAresta('a25', '7', '5')
        self.g_grande_dfs1.adicionaAresta('a26', '23', '22')
        self.g_grande_dfs1.adicionaAresta('a27', '22', '21')
        self.g_grande_dfs1.adicionaAresta('a28', '21', '20')
        self.g_grande_dfs1.adicionaAresta('a29', '20', '19')
        self.g_grande_dfs1.adicionaAresta('a30', '19', '17')
        self.g_grande_dfs1.adicionaAresta('a31', '17', '16')
        self.g_grande_dfs1.adicionaAresta('a32', '17', '18')
        self.g_grande_dfs1.adicionaAresta('a35', '10', '9')
        self.g_grande_dfs1.adicionaAresta('a36', '10', '11')

        self.g_grande_dfs23 = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
             '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
             '24', '25', '26', '27', '28', '29', '30'])
        self.g_grande_dfs23.adicionaAresta('a1', '1', '2')
        self.g_grande_dfs23.adicionaAresta('a2', '2', '3')
        self.g_grande_dfs23.adicionaAresta('a3', '1', '4')
        self.g_grande_dfs23.adicionaAresta('a5', '3', '5')
        self.g_grande_dfs23.adicionaAresta('a6', '3', '8')
        self.g_grande_dfs23.adicionaAresta('a7', '8', '12')
        self.g_grande_dfs23.adicionaAresta('a10', '12', '13')
        self.g_grande_dfs23.adicionaAresta('a11', '13', '14')
        self.g_grande_dfs23.adicionaAresta('a12', '14', '16')
        self.g_grande_dfs23.adicionaAresta('a13', '14', '15')
        self.g_grande_dfs23.adicionaAresta('a14', '4', '6')
        self.g_grande_dfs23.adicionaAresta('a15', '6', '30')
        self.g_grande_dfs23.adicionaAresta('a16', '30', '29')
        self.g_grande_dfs23.adicionaAresta('a17', '29', '28')
        self.g_grande_dfs23.adicionaAresta('a18', '28', '25')
        self.g_grande_dfs23.adicionaAresta('a19', '28', '27')
        self.g_grande_dfs23.adicionaAresta('a20', '27', '26')
        self.g_grande_dfs23.adicionaAresta('a22', '25', '23')
        self.g_grande_dfs23.adicionaAresta('a23', '23', '24')
        self.g_grande_dfs23.adicionaAresta('a25', '7', '5')
        self.g_grande_dfs23.adicionaAresta('a27', '22', '21')
        self.g_grande_dfs23.adicionaAresta('a28', '21', '20')
        self.g_grande_dfs23.adicionaAresta('a29', '20', '19')
        self.g_grande_dfs23.adicionaAresta('a30', '19', '17')
        self.g_grande_dfs23.adicionaAresta('a31', '17', '16')
        self.g_grande_dfs23.adicionaAresta('a33', '18', '19')
        self.g_grande_dfs23.adicionaAresta('a34', '20', '10')
        self.g_grande_dfs23.adicionaAresta('a35', '10', '9')
        self.g_grande_dfs23.adicionaAresta('a36', '10', '11')

        # Grafos para teste de BFS
        self.g_medio_bfs1 = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.g_medio_bfs1.adicionaAresta('a1', '1', '2')
        self.g_medio_bfs1.adicionaAresta('a2', '1', '3')
        self.g_medio_bfs1.adicionaAresta('a3', '3', '4')
        self.g_medio_bfs1.adicionaAresta('a5', '5', '6')
        self.g_medio_bfs1.adicionaAresta('a6', '2', '6')
        self.g_medio_bfs1.adicionaAresta('a7', '2', '7')
        self.g_medio_bfs1.adicionaAresta('a9', '7', '8')
        self.g_medio_bfs1.adicionaAresta('a10', '8', '9')
        self.g_medio_bfs1.adicionaAresta('a11', '8', '10')

        self.g_medio_bfs5 = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.g_medio_bfs5.adicionaAresta('a2', '1', '3')
        self.g_medio_bfs5.adicionaAresta('a3', '3', '4')
        self.g_medio_bfs5.adicionaAresta('a4', '4', '5')
        self.g_medio_bfs5.adicionaAresta('a5', '5', '6')
        self.g_medio_bfs5.adicionaAresta('a6', '2', '6')
        self.g_medio_bfs5.adicionaAresta('a8', '6', '7')
        self.g_medio_bfs5.adicionaAresta('a9', '7', '8')
        self.g_medio_bfs5.adicionaAresta('a10', '8', '9')
        self.g_medio_bfs5.adicionaAresta('a11', '8', '10')

        self.g_medio_bfs7 = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.g_medio_bfs7.adicionaAresta('a1', '1', '2')
        self.g_medio_bfs7.adicionaAresta('a2', '1', '3')
        self.g_medio_bfs7.adicionaAresta('a4', '4', '5')
        self.g_medio_bfs7.adicionaAresta('a5', '5', '6')
        self.g_medio_bfs7.adicionaAresta('a7', '2', '7')
        self.g_medio_bfs7.adicionaAresta('a8', '6', '7')
        self.g_medio_bfs7.adicionaAresta('a9', '7', '8')
        self.g_medio_bfs7.adicionaAresta('a10', '8', '9')
        self.g_medio_bfs7.adicionaAresta('a11', '8', '10')

        self.g_medio_bfs9 = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.g_medio_bfs9.adicionaAresta('a1', '1', '2')
        self.g_medio_bfs9.adicionaAresta('a2', '1', '3')
        self.g_medio_bfs9.adicionaAresta('a4', '4', '5')
        self.g_medio_bfs9.adicionaAresta('a5', '5', '6')
        self.g_medio_bfs9.adicionaAresta('a7', '2', '7')
        self.g_medio_bfs9.adicionaAresta('a8', '6', '7')
        self.g_medio_bfs9.adicionaAresta('a9', '7', '8')
        self.g_medio_bfs9.adicionaAresta('a10', '8', '9')
        self.g_medio_bfs9.adicionaAresta('a12', '9', '10')

        self.g_grande_bfs1 = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
             '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
             '24', '25', '26', '27', '28', '29', '30'])
        self.g_grande_bfs1.adicionaAresta('a1', '1', '2')
        self.g_grande_bfs1.adicionaAresta('a2', '2', '3')
        self.g_grande_bfs1.adicionaAresta('a3', '1', '4')
        self.g_grande_bfs1.adicionaAresta('a5', '3', '5')
        self.g_grande_bfs1.adicionaAresta('a6', '3', '8')
        self.g_grande_bfs1.adicionaAresta('a7', '8', '12')
        self.g_grande_bfs1.adicionaAresta('a8', '8', '9')
        self.g_grande_bfs1.adicionaAresta('a9', '8', '11')
        self.g_grande_bfs1.adicionaAresta('a10', '12', '13')
        self.g_grande_bfs1.adicionaAresta('a11', '13', '14')
        self.g_grande_bfs1.adicionaAresta('a12', '14', '16')
        self.g_grande_bfs1.adicionaAresta('a13', '14', '15')
        self.g_grande_bfs1.adicionaAresta('a14', '4', '6')
        self.g_grande_bfs1.adicionaAresta('a15', '6', '30')
        self.g_grande_bfs1.adicionaAresta('a16', '30', '29')
        self.g_grande_bfs1.adicionaAresta('a17', '29', '28')
        self.g_grande_bfs1.adicionaAresta('a19', '28', '27')
        self.g_grande_bfs1.adicionaAresta('a21', '26', '25')
        self.g_grande_bfs1.adicionaAresta('a22', '25', '23')
        self.g_grande_bfs1.adicionaAresta('a23', '23', '24')
        self.g_grande_bfs1.adicionaAresta('a24', '23', '7')
        self.g_grande_bfs1.adicionaAresta('a25', '7', '5')
        self.g_grande_bfs1.adicionaAresta('a26', '23', '22')
        self.g_grande_bfs1.adicionaAresta('a27', '22', '21')
        self.g_grande_bfs1.adicionaAresta('a29', '20', '19')
        self.g_grande_bfs1.adicionaAresta('a31', '17', '16')
        self.g_grande_bfs1.adicionaAresta('a33', '19', '18')
        self.g_grande_bfs1.adicionaAresta('a34', '20', '10')
        self.g_grande_bfs1.adicionaAresta('a35', '10', '9')

        self.g_grande_bfs23 = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
             '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
             '24', '25', '26', '27', '28', '29', '30'])
        self.g_grande_bfs23.adicionaAresta('a1', '1', '2')
        self.g_grande_bfs23.adicionaAresta('a2', '2', '3')
        self.g_grande_bfs23.adicionaAresta('a4', '3', '4')
        self.g_grande_bfs23.adicionaAresta('a5', '3', '5')
        self.g_grande_bfs23.adicionaAresta('a6', '3', '8')
        self.g_grande_bfs23.adicionaAresta('a7', '8', '12')
        self.g_grande_bfs23.adicionaAresta('a8', '8', '9')
        self.g_grande_bfs23.adicionaAresta('a9', '8', '11')
        self.g_grande_bfs23.adicionaAresta('a10', '12', '13')
        self.g_grande_bfs23.adicionaAresta('a11', '13', '14')
        self.g_grande_bfs23.adicionaAresta('a13', '14', '15')
        self.g_grande_bfs23.adicionaAresta('a15', '6', '30')
        self.g_grande_bfs23.adicionaAresta('a16', '30', '29')
        self.g_grande_bfs23.adicionaAresta('a17', '29', '28')
        self.g_grande_bfs23.adicionaAresta('a18', '28', '25')
        self.g_grande_bfs23.adicionaAresta('a19', '28', '27')
        self.g_grande_bfs23.adicionaAresta('a21', '26', '25')
        self.g_grande_bfs23.adicionaAresta('a22', '25', '23')
        self.g_grande_bfs23.adicionaAresta('a23', '23', '24')
        self.g_grande_bfs23.adicionaAresta('a24', '23', '7')
        self.g_grande_bfs23.adicionaAresta('a25', '7', '5')
        self.g_grande_bfs23.adicionaAresta('a26', '23', '22')
        self.g_grande_bfs23.adicionaAresta('a27', '22', '21')
        self.g_grande_bfs23.adicionaAresta('a28', '21', '20')
        self.g_grande_bfs23.adicionaAresta('a29', '20', '19')
        self.g_grande_bfs23.adicionaAresta('a30', '19', '17')
        self.g_grande_bfs23.adicionaAresta('a31', '17', '16')
        self.g_grande_bfs23.adicionaAresta('a33', '18', '19')
        self.g_grande_bfs23.adicionaAresta('a34', '20', '10')

        # Grafos com ciclo
        self.com = MeuGrafo(['1', '2', '3', '4'])
        self.com.adicionaAresta('a1', '1', '2')
        self.com.adicionaAresta('a2', '1', '3')
        self.com.adicionaAresta('a3', '2', '4')
        self.com.adicionaAresta('a4', '3', '4')

        self.com2 = MeuGrafo(['1', '2'])
        self.com2.adicionaAresta('a1', '1', '2')
        self.com2.adicionaAresta('a2', '1', '2')

        self.com3 = MeuGrafo(['1'])
        self.com3.adicionaAresta('a1', '1', '1')

        # Grafos sem ciclo
        self.sem = MeuGrafo(['1', '2', '3', '4', '5'])
        self.sem.adicionaAresta('a1', '1', '2')
        self.sem.adicionaAresta('a2', '1', '3')
        self.sem.adicionaAresta('a3', '3', '4')
        self.sem.adicionaAresta('a4', '3', '5')

        # Grafos para teste de caminho euleriano
        self.slays = MeuGrafo(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
        self.slays.adicionaAresta('a1', 'a', 'b')
        self.slays.adicionaAresta('a2', 'a', 'c')
        self.slays.adicionaAresta('a3', 'a', 'd')
        self.slays.adicionaAresta('a4', 'a', 'f')
        self.slays.adicionaAresta('a5', 'b', 'c')
        self.slays.adicionaAresta('a6', 'b', 'g')
        self.slays.adicionaAresta('a7', 'b', 'e')
        self.slays.adicionaAresta('a8', 'e', 'f')
        self.slays.adicionaAresta('a9', 'f', 'g')

        self.teste_conexo = MeuGrafo(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
        self.teste_conexo.adicionaAresta('a1', 'a', 'b')
        self.teste_conexo.adicionaAresta('a2', 'a', 'd')
        self.teste_conexo.adicionaAresta('a3', 'b', 'c')
        self.teste_conexo.adicionaAresta('a4', 'c', 'd')
        self.teste_conexo.adicionaAresta('a5', 'd', 'e')
        self.teste_conexo.adicionaAresta('a6', 'e', 'f')
        self.teste_conexo.adicionaAresta('a7', 'e', 'h')
        self.teste_conexo.adicionaAresta('a8', 'f', 'g')
        self.teste_conexo.adicionaAresta('a9', 'g', 'h')

        self.teste_desconexo = MeuGrafo([
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
        self.teste_desconexo.adicionaAresta('a1', 'a', 'b')
        self.teste_desconexo.adicionaAresta('a2', 'a', 'd')
        self.teste_desconexo.adicionaAresta('a3', 'b', 'c')
        self.teste_desconexo.adicionaAresta('a4', 'c', 'd')
        self.teste_desconexo.adicionaAresta('a6', 'e', 'f')
        self.teste_desconexo.adicionaAresta('a7', 'e', 'h')
        self.teste_desconexo.adicionaAresta('a8', 'f', 'g')
        self.teste_desconexo.adicionaAresta('a9', 'g', 'h')

        self.pares = MeuGrafo(['a', 'b', 'c', 'd', 'e', 'f'])
        self.pares.adicionaAresta('a1', 'a', 'b')
        self.pares.adicionaAresta('a2', 'a', 'f')
        self.pares.adicionaAresta('a3', 'b', 'c')
        self.pares.adicionaAresta('a4', 'c', 'd')
        self.pares.adicionaAresta('a5', 'd', 'e')
        self.pares.adicionaAresta('a6', 'e', 'f')

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(
             bibgrafo.grafo_exceptions.ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(
             bibgrafo.grafo_exceptions.ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(
             bibgrafo.grafo_exceptions.ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(
             bibgrafo.grafo_exceptions.ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(
             bibgrafo.grafo_exceptions.ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(
             bibgrafo.grafo_exceptions.ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         ['J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P',
                          'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z', 'M-Z'])
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), [])
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(
             bibgrafo.grafo_exceptions.VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice
        # para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), {'a1'})
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')),
                         {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')),
                         {'a7', 'a8'})
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')),
                         {'a1', 'a2', 'a3'})
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), {'asd'})
        with self.assertRaises(
             bibgrafo.grafo_exceptions.VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse(self.g_p_sem_paralelas.eh_completo())
        self.assertTrue(self.g_c.eh_completo())
        self.assertTrue(self.g_c2.eh_completo())
        self.assertTrue(self.g_c3.eh_completo())
        self.assertFalse(self.g_l1.eh_completo())
        self.assertFalse(self.g_l2.eh_completo())
        self.assertFalse(self.g_l3.eh_completo())
        self.assertFalse(self.g_l4.eh_completo())
        self.assertFalse(self.g_l5.eh_completo())

    def test_conexo(self):
        self.assertTrue(self.g_p.conexo())
        self.assertTrue(self.g_c.conexo())
        self.assertTrue(self.g_c2.conexo())
        self.assertTrue(self.g_c3.conexo())
        self.assertTrue(self.g_pequeno.conexo())
        self.assertTrue(self.g_medio.conexo())
        self.assertTrue(self.g_grande.conexo())
        self.assertTrue(self.g_pequeno.conexo())
        self.assertTrue(self.g_medio.conexo())
        self.assertTrue(self.g_grande.conexo())
        self.assertFalse(self.g_d.conexo())
        self.assertFalse(self.outro.conexo())

    def test_caminho_euleriano(self):
        self.assertEqual(self.g_medio_dfs5.caminho_euleriano(),
                         ['5', 'a4', '4', 'a3', '3', 'a2', '1', 'a1',
                          '2', 'a6', '6', 'a8', '7', 'a9', '8', 'a10', '9',
                          'a12', '10'])
        self.assertEqual(self.g_medio_dfs7.caminho_euleriano(),
                         ['6', 'a5', '5', 'a4', '4', 'a3', '3', 'a2',
                          '1', 'a1', '2', 'a7', '7', 'a9', '8', 'a10', '9',
                          'a12', '10'])
        self.assertEqual(self.com.caminho_euleriano(), ['1', 'a1', '2',
                                                        'a3', '4', 'a4', '3',
                                                        'a2', '1'])
        self.assertEqual(self.com2.caminho_euleriano(),
                         ['1', 'a1', '2', 'a2', '1'])
        self.assertEqual(self.com3.caminho_euleriano(), ['1', 'a1', '1'])
        self.assertEqual(self.g_c2.caminho_euleriano(),
                         ['Nina', 'amiga', 'Maria'])
        self.assertEqual(self.slays.caminho_euleriano(),
                         ['d', 'a3', 'a', 'a1', 'b', 'a5',
                          'c', 'a2', 'a', 'a4', 'f', 'a8',
                          'e', 'a7', 'b', 'a6', 'g', 'a9', 'f'])
        self.assertEqual(self.teste_conexo.caminho_euleriano(),
                         ['d', 'a2', 'a', 'a1', 'b', 'a3', 'c',
                          'a4', 'd', 'a5', 'e', 'a6', 'f', 'a8', 'g', 'a9',
                          'h', 'a7', 'e'])
        self.assertEqual(self.pares.caminho_euleriano(),
                         ['a', 'a1', 'b', 'a3', 'c', 'a4', 'd', 'a5',
                          'e', 'a6', 'f', 'a2', 'a'])
        self.assertFalse(self.g_p.caminho_euleriano())
        self.assertFalse(self.g_p_sem_paralelas.caminho_euleriano())
        self.assertFalse(self.g_c.caminho_euleriano())
        self.assertFalse(self.g_c3.caminho_euleriano())
        self.assertFalse(self.teste_desconexo.caminho_euleriano())


if __name__ == '__main__':
    unittest.main()
