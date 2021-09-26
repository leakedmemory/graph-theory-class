import unittest

from bibgrafo import grafo_exceptions

from meu_grafo_matriz_adjacencia_dir import MeuGrafo


class TestGrafo(unittest.TestCase):
    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(["J", "C", "E", "P", "M", "T", "Z"])
        self.g_p.adicionaAresta("a1", "J", "C")
        self.g_p.adicionaAresta("a2", "C", "E")
        self.g_p.adicionaAresta("a3", "C", "E")
        self.g_p.adicionaAresta("a4", "P", "C")
        self.g_p.adicionaAresta("a5", "P", "C")
        self.g_p.adicionaAresta("a6", "T", "C")
        self.g_p.adicionaAresta("a7", "M", "C")
        self.g_p.adicionaAresta("a8", "M", "T")
        self.g_p.adicionaAresta("a9", "T", "Z")

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(["J", "C", "E", "P", "M", "T", "Z"])
        self.g_p_sem_paralelas.adicionaAresta("a1", "J", "C")
        self.g_p_sem_paralelas.adicionaAresta("a2", "C", "E")
        self.g_p_sem_paralelas.adicionaAresta("a3", "P", "C")
        self.g_p_sem_paralelas.adicionaAresta("a4", "T", "C")
        self.g_p_sem_paralelas.adicionaAresta("a5", "M", "C")
        self.g_p_sem_paralelas.adicionaAresta("a6", "M", "T")
        self.g_p_sem_paralelas.adicionaAresta("a7", "T", "Z")

        # Grafos completos
        self.g_c = MeuGrafo(["J", "C", "E", "P"])
        self.g_c.adicionaAresta("a1", "J", "C")
        self.g_c.adicionaAresta("a2", "J", "E")
        self.g_c.adicionaAresta("a3", "J", "P")
        self.g_c.adicionaAresta("a4", "E", "C")
        self.g_c.adicionaAresta("a5", "P", "C")
        self.g_c.adicionaAresta("a6", "P", "E")

        self.g_c2 = MeuGrafo(["Nina", "Maria"])
        self.g_c2.adicionaAresta("amiga", "Nina", "Maria")

        self.g_c3 = MeuGrafo(["J"])

        # Grafos com laco
        self.g_l1 = MeuGrafo(["A", "B", "C", "D"])
        self.g_l1.adicionaAresta("a1", "A", "A")
        self.g_l1.adicionaAresta("a2", "A", "B")
        self.g_l1.adicionaAresta("a3", "A", "A")

        self.g_l2 = MeuGrafo(["A", "B", "C", "D"])
        self.g_l2.adicionaAresta("a1", "A", "B")
        self.g_l2.adicionaAresta("a2", "B", "B")
        self.g_l2.adicionaAresta("a3", "B", "A")

        self.g_l3 = MeuGrafo(["A", "B", "C", "D"])
        self.g_l3.adicionaAresta("a1", "C", "A")
        self.g_l3.adicionaAresta("a2", "C", "C")
        self.g_l3.adicionaAresta("a3", "D", "D")
        self.g_l3.adicionaAresta("a4", "D", "D")

        self.g_l4 = MeuGrafo(["D"])
        self.g_l4.adicionaAresta("a1", "D", "D")

        self.g_l5 = MeuGrafo(["C", "D"])
        self.g_l5.adicionaAresta("a1", "D", "C")
        self.g_l5.adicionaAresta("a2", "C", "C")

        # Grafos desconexos
        self.g_d = MeuGrafo(["A", "B", "C", "D"])
        self.g_d.adicionaAresta("asd", "A", "B")

        self.outro = MeuGrafo(["1", "2", "3", "4", "5", "6"])
        self.outro.adicionaAresta("a1", "1", "2")
        self.outro.adicionaAresta("a2", "2", "3")
        self.outro.adicionaAresta("a3", "3", "4")
        self.outro.adicionaAresta("a4", "4", "5")

        # Grafos pai para exemplo teste
        self.g_pequeno = MeuGrafo(["1", "2", "3", "4", "5"])
        self.g_pequeno.adicionaAresta("a1", "1", "2")
        self.g_pequeno.adicionaAresta("a2", "1", "3")
        self.g_pequeno.adicionaAresta("a3", "2", "4")
        self.g_pequeno.adicionaAresta("a4", "2", "5")

        self.g_medio = MeuGrafo(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
        self.g_medio.adicionaAresta("a1", "1", "2")
        self.g_medio.adicionaAresta("a2", "1", "3")
        self.g_medio.adicionaAresta("a3", "3", "4")
        self.g_medio.adicionaAresta("a4", "4", "5")
        self.g_medio.adicionaAresta("a5", "5", "6")
        self.g_medio.adicionaAresta("a6", "2", "6")
        self.g_medio.adicionaAresta("a7", "2", "7")
        self.g_medio.adicionaAresta("a8", "6", "7")
        self.g_medio.adicionaAresta("a9", "7", "8")
        self.g_medio.adicionaAresta("a10", "8", "9")
        self.g_medio.adicionaAresta("a11", "8", "10")
        self.g_medio.adicionaAresta("a12", "9", "10")

        self.g_grande = MeuGrafo(
            [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
                "30",
            ]
        )
        self.g_grande.adicionaAresta("a1", "1", "2")
        self.g_grande.adicionaAresta("a2", "2", "3")
        self.g_grande.adicionaAresta("a3", "1", "4")
        self.g_grande.adicionaAresta("a4", "3", "4")
        self.g_grande.adicionaAresta("a5", "3", "5")
        self.g_grande.adicionaAresta("a6", "3", "8")
        self.g_grande.adicionaAresta("a7", "8", "12")
        self.g_grande.adicionaAresta("a8", "8", "9")
        self.g_grande.adicionaAresta("a9", "8", "11")
        self.g_grande.adicionaAresta("a10", "12", "13")
        self.g_grande.adicionaAresta("a11", "13", "14")
        self.g_grande.adicionaAresta("a12", "14", "16")
        self.g_grande.adicionaAresta("a13", "14", "15")
        self.g_grande.adicionaAresta("a14", "4", "6")
        self.g_grande.adicionaAresta("a15", "6", "30")
        self.g_grande.adicionaAresta("a16", "30", "29")
        self.g_grande.adicionaAresta("a17", "29", "28")
        self.g_grande.adicionaAresta("a18", "28", "25")
        self.g_grande.adicionaAresta("a19", "28", "27")
        self.g_grande.adicionaAresta("a20", "27", "26")
        self.g_grande.adicionaAresta("a21", "26", "25")
        self.g_grande.adicionaAresta("a22", "25", "23")
        self.g_grande.adicionaAresta("a23", "23", "24")
        self.g_grande.adicionaAresta("a24", "23", "7")
        self.g_grande.adicionaAresta("a25", "7", "5")
        self.g_grande.adicionaAresta("a26", "23", "22")
        self.g_grande.adicionaAresta("a27", "22", "21")
        self.g_grande.adicionaAresta("a28", "21", "20")
        self.g_grande.adicionaAresta("a29", "20", "19")
        self.g_grande.adicionaAresta("a30", "19", "17")
        self.g_grande.adicionaAresta("a31", "17", "16")
        self.g_grande.adicionaAresta("a32", "17", "18")
        self.g_grande.adicionaAresta("a33", "18", "19")
        self.g_grande.adicionaAresta("a34", "20", "10")
        self.g_grande.adicionaAresta("a35", "10", "9")
        self.g_grande.adicionaAresta("a36", "10", "11")

        # Grafos para teste de DFS
        self.g_medio_dfs1 = MeuGrafo(
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        )
        self.g_medio_dfs1.adicionaAresta("a1", "1", "2")
        self.g_medio_dfs1.adicionaAresta("a3", "3", "4")
        self.g_medio_dfs1.adicionaAresta("a4", "4", "5")
        self.g_medio_dfs1.adicionaAresta("a5", "5", "6")
        self.g_medio_dfs1.adicionaAresta("a6", "2", "6")
        self.g_medio_dfs1.adicionaAresta("a8", "6", "7")
        self.g_medio_dfs1.adicionaAresta("a9", "7", "8")
        self.g_medio_dfs1.adicionaAresta("a10", "8", "9")
        self.g_medio_dfs1.adicionaAresta("a12", "9", "10")

        self.g_medio_dfs5 = MeuGrafo(
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        )
        self.g_medio_dfs5.adicionaAresta("a1", "1", "2")
        self.g_medio_dfs5.adicionaAresta("a2", "1", "3")
        self.g_medio_dfs5.adicionaAresta("a3", "3", "4")
        self.g_medio_dfs5.adicionaAresta("a4", "4", "5")
        self.g_medio_dfs5.adicionaAresta("a6", "2", "6")
        self.g_medio_dfs5.adicionaAresta("a8", "6", "7")
        self.g_medio_dfs5.adicionaAresta("a9", "7", "8")
        self.g_medio_dfs5.adicionaAresta("a10", "8", "9")
        self.g_medio_dfs5.adicionaAresta("a12", "9", "10")

        self.g_medio_dfs7 = MeuGrafo(
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        )
        self.g_medio_dfs7.adicionaAresta("a1", "1", "2")
        self.g_medio_dfs7.adicionaAresta("a2", "1", "3")
        self.g_medio_dfs7.adicionaAresta("a3", "3", "4")
        self.g_medio_dfs7.adicionaAresta("a4", "4", "5")
        self.g_medio_dfs7.adicionaAresta("a5", "5", "6")
        self.g_medio_dfs7.adicionaAresta("a7", "2", "7")
        self.g_medio_dfs7.adicionaAresta("a9", "7", "8")
        self.g_medio_dfs7.adicionaAresta("a10", "8", "9")
        self.g_medio_dfs7.adicionaAresta("a12", "9", "10")

        self.g_medio_dfs9 = MeuGrafo(
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        )
        self.g_medio_dfs9.adicionaAresta("a1", "1", "2")
        self.g_medio_dfs9.adicionaAresta("a2", "1", "3")
        self.g_medio_dfs9.adicionaAresta("a3", "3", "4")
        self.g_medio_dfs9.adicionaAresta("a4", "4", "5")
        self.g_medio_dfs9.adicionaAresta("a5", "5", "6")
        self.g_medio_dfs9.adicionaAresta("a7", "2", "7")
        self.g_medio_dfs9.adicionaAresta("a9", "7", "8")
        self.g_medio_dfs9.adicionaAresta("a10", "8", "9")
        self.g_medio_dfs9.adicionaAresta("a11", "8", "10")

        self.g_grande_dfs1 = MeuGrafo(
            [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
                "30",
            ]
        )
        self.g_grande_dfs1.adicionaAresta("a1", "1", "2")
        self.g_grande_dfs1.adicionaAresta("a2", "2", "3")
        self.g_grande_dfs1.adicionaAresta("a4", "3", "4")
        self.g_grande_dfs1.adicionaAresta("a7", "8", "12")
        self.g_grande_dfs1.adicionaAresta("a8", "8", "9")
        self.g_grande_dfs1.adicionaAresta("a10", "12", "13")
        self.g_grande_dfs1.adicionaAresta("a11", "13", "14")
        self.g_grande_dfs1.adicionaAresta("a12", "14", "16")
        self.g_grande_dfs1.adicionaAresta("a13", "14", "15")
        self.g_grande_dfs1.adicionaAresta("a14", "4", "6")
        self.g_grande_dfs1.adicionaAresta("a15", "6", "30")
        self.g_grande_dfs1.adicionaAresta("a16", "30", "29")
        self.g_grande_dfs1.adicionaAresta("a17", "29", "28")
        self.g_grande_dfs1.adicionaAresta("a18", "28", "25")
        self.g_grande_dfs1.adicionaAresta("a20", "27", "26")
        self.g_grande_dfs1.adicionaAresta("a21", "26", "25")
        self.g_grande_dfs1.adicionaAresta("a22", "25", "23")
        self.g_grande_dfs1.adicionaAresta("a23", "23", "24")
        self.g_grande_dfs1.adicionaAresta("a24", "23", "7")
        self.g_grande_dfs1.adicionaAresta("a25", "7", "5")
        self.g_grande_dfs1.adicionaAresta("a26", "23", "22")
        self.g_grande_dfs1.adicionaAresta("a27", "22", "21")
        self.g_grande_dfs1.adicionaAresta("a28", "21", "20")
        self.g_grande_dfs1.adicionaAresta("a29", "20", "19")
        self.g_grande_dfs1.adicionaAresta("a30", "19", "17")
        self.g_grande_dfs1.adicionaAresta("a31", "17", "16")
        self.g_grande_dfs1.adicionaAresta("a32", "17", "18")
        self.g_grande_dfs1.adicionaAresta("a35", "10", "9")
        self.g_grande_dfs1.adicionaAresta("a36", "10", "11")

        self.g_grande_dfs23 = MeuGrafo(
            [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
                "30",
            ]
        )
        self.g_grande_dfs23.adicionaAresta("a1", "1", "2")
        self.g_grande_dfs23.adicionaAresta("a2", "2", "3")
        self.g_grande_dfs23.adicionaAresta("a3", "1", "4")
        self.g_grande_dfs23.adicionaAresta("a5", "3", "5")
        self.g_grande_dfs23.adicionaAresta("a6", "3", "8")
        self.g_grande_dfs23.adicionaAresta("a7", "8", "12")
        self.g_grande_dfs23.adicionaAresta("a10", "12", "13")
        self.g_grande_dfs23.adicionaAresta("a11", "13", "14")
        self.g_grande_dfs23.adicionaAresta("a12", "14", "16")
        self.g_grande_dfs23.adicionaAresta("a13", "14", "15")
        self.g_grande_dfs23.adicionaAresta("a14", "4", "6")
        self.g_grande_dfs23.adicionaAresta("a15", "6", "30")
        self.g_grande_dfs23.adicionaAresta("a16", "30", "29")
        self.g_grande_dfs23.adicionaAresta("a17", "29", "28")
        self.g_grande_dfs23.adicionaAresta("a18", "28", "25")
        self.g_grande_dfs23.adicionaAresta("a19", "28", "27")
        self.g_grande_dfs23.adicionaAresta("a20", "27", "26")
        self.g_grande_dfs23.adicionaAresta("a22", "25", "23")
        self.g_grande_dfs23.adicionaAresta("a23", "23", "24")
        self.g_grande_dfs23.adicionaAresta("a25", "7", "5")
        self.g_grande_dfs23.adicionaAresta("a27", "22", "21")
        self.g_grande_dfs23.adicionaAresta("a28", "21", "20")
        self.g_grande_dfs23.adicionaAresta("a29", "20", "19")
        self.g_grande_dfs23.adicionaAresta("a30", "19", "17")
        self.g_grande_dfs23.adicionaAresta("a31", "17", "16")
        self.g_grande_dfs23.adicionaAresta("a33", "18", "19")
        self.g_grande_dfs23.adicionaAresta("a34", "20", "10")
        self.g_grande_dfs23.adicionaAresta("a35", "10", "9")
        self.g_grande_dfs23.adicionaAresta("a36", "10", "11")

        # Grafos para teste de BFS
        self.g_medio_bfs1 = MeuGrafo(
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        )
        self.g_medio_bfs1.adicionaAresta("a1", "1", "2")
        self.g_medio_bfs1.adicionaAresta("a2", "1", "3")
        self.g_medio_bfs1.adicionaAresta("a3", "3", "4")
        self.g_medio_bfs1.adicionaAresta("a5", "5", "6")
        self.g_medio_bfs1.adicionaAresta("a6", "2", "6")
        self.g_medio_bfs1.adicionaAresta("a7", "2", "7")
        self.g_medio_bfs1.adicionaAresta("a9", "7", "8")
        self.g_medio_bfs1.adicionaAresta("a10", "8", "9")
        self.g_medio_bfs1.adicionaAresta("a11", "8", "10")

        self.g_medio_bfs5 = MeuGrafo(
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        )
        self.g_medio_bfs5.adicionaAresta("a2", "1", "3")
        self.g_medio_bfs5.adicionaAresta("a3", "3", "4")
        self.g_medio_bfs5.adicionaAresta("a4", "4", "5")
        self.g_medio_bfs5.adicionaAresta("a5", "5", "6")
        self.g_medio_bfs5.adicionaAresta("a6", "2", "6")
        self.g_medio_bfs5.adicionaAresta("a8", "6", "7")
        self.g_medio_bfs5.adicionaAresta("a9", "7", "8")
        self.g_medio_bfs5.adicionaAresta("a10", "8", "9")
        self.g_medio_bfs5.adicionaAresta("a11", "8", "10")

        self.g_medio_bfs7 = MeuGrafo(
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        )
        self.g_medio_bfs7.adicionaAresta("a1", "1", "2")
        self.g_medio_bfs7.adicionaAresta("a2", "1", "3")
        self.g_medio_bfs7.adicionaAresta("a4", "4", "5")
        self.g_medio_bfs7.adicionaAresta("a5", "5", "6")
        self.g_medio_bfs7.adicionaAresta("a7", "2", "7")
        self.g_medio_bfs7.adicionaAresta("a8", "6", "7")
        self.g_medio_bfs7.adicionaAresta("a9", "7", "8")
        self.g_medio_bfs7.adicionaAresta("a10", "8", "9")
        self.g_medio_bfs7.adicionaAresta("a11", "8", "10")

        self.g_medio_bfs9 = MeuGrafo(
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        )
        self.g_medio_bfs9.adicionaAresta("a1", "1", "2")
        self.g_medio_bfs9.adicionaAresta("a2", "1", "3")
        self.g_medio_bfs9.adicionaAresta("a4", "4", "5")
        self.g_medio_bfs9.adicionaAresta("a5", "5", "6")
        self.g_medio_bfs9.adicionaAresta("a7", "2", "7")
        self.g_medio_bfs9.adicionaAresta("a8", "6", "7")
        self.g_medio_bfs9.adicionaAresta("a9", "7", "8")
        self.g_medio_bfs9.adicionaAresta("a10", "8", "9")
        self.g_medio_bfs9.adicionaAresta("a12", "9", "10")

        self.g_grande_bfs1 = MeuGrafo(
            [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
                "30",
            ]
        )
        self.g_grande_bfs1.adicionaAresta("a1", "1", "2")
        self.g_grande_bfs1.adicionaAresta("a2", "2", "3")
        self.g_grande_bfs1.adicionaAresta("a3", "1", "4")
        self.g_grande_bfs1.adicionaAresta("a5", "3", "5")
        self.g_grande_bfs1.adicionaAresta("a6", "3", "8")
        self.g_grande_bfs1.adicionaAresta("a7", "8", "12")
        self.g_grande_bfs1.adicionaAresta("a8", "8", "9")
        self.g_grande_bfs1.adicionaAresta("a9", "8", "11")
        self.g_grande_bfs1.adicionaAresta("a10", "12", "13")
        self.g_grande_bfs1.adicionaAresta("a11", "13", "14")
        self.g_grande_bfs1.adicionaAresta("a12", "14", "16")
        self.g_grande_bfs1.adicionaAresta("a13", "14", "15")
        self.g_grande_bfs1.adicionaAresta("a14", "4", "6")
        self.g_grande_bfs1.adicionaAresta("a15", "6", "30")
        self.g_grande_bfs1.adicionaAresta("a16", "30", "29")
        self.g_grande_bfs1.adicionaAresta("a17", "29", "28")
        self.g_grande_bfs1.adicionaAresta("a19", "28", "27")
        self.g_grande_bfs1.adicionaAresta("a21", "26", "25")
        self.g_grande_bfs1.adicionaAresta("a22", "25", "23")
        self.g_grande_bfs1.adicionaAresta("a23", "23", "24")
        self.g_grande_bfs1.adicionaAresta("a24", "23", "7")
        self.g_grande_bfs1.adicionaAresta("a25", "7", "5")
        self.g_grande_bfs1.adicionaAresta("a26", "23", "22")
        self.g_grande_bfs1.adicionaAresta("a27", "22", "21")
        self.g_grande_bfs1.adicionaAresta("a29", "20", "19")
        self.g_grande_bfs1.adicionaAresta("a31", "17", "16")
        self.g_grande_bfs1.adicionaAresta("a33", "19", "18")
        self.g_grande_bfs1.adicionaAresta("a34", "20", "10")
        self.g_grande_bfs1.adicionaAresta("a35", "10", "9")

        self.g_grande_bfs23 = MeuGrafo(
            [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
                "30",
            ]
        )
        self.g_grande_bfs23.adicionaAresta("a1", "1", "2")
        self.g_grande_bfs23.adicionaAresta("a2", "2", "3")
        self.g_grande_bfs23.adicionaAresta("a4", "3", "4")
        self.g_grande_bfs23.adicionaAresta("a5", "3", "5")
        self.g_grande_bfs23.adicionaAresta("a6", "3", "8")
        self.g_grande_bfs23.adicionaAresta("a7", "8", "12")
        self.g_grande_bfs23.adicionaAresta("a8", "8", "9")
        self.g_grande_bfs23.adicionaAresta("a9", "8", "11")
        self.g_grande_bfs23.adicionaAresta("a10", "12", "13")
        self.g_grande_bfs23.adicionaAresta("a11", "13", "14")
        self.g_grande_bfs23.adicionaAresta("a13", "14", "15")
        self.g_grande_bfs23.adicionaAresta("a15", "6", "30")
        self.g_grande_bfs23.adicionaAresta("a16", "30", "29")
        self.g_grande_bfs23.adicionaAresta("a17", "29", "28")
        self.g_grande_bfs23.adicionaAresta("a18", "28", "25")
        self.g_grande_bfs23.adicionaAresta("a19", "28", "27")
        self.g_grande_bfs23.adicionaAresta("a21", "26", "25")
        self.g_grande_bfs23.adicionaAresta("a22", "25", "23")
        self.g_grande_bfs23.adicionaAresta("a23", "23", "24")
        self.g_grande_bfs23.adicionaAresta("a24", "23", "7")
        self.g_grande_bfs23.adicionaAresta("a25", "7", "5")
        self.g_grande_bfs23.adicionaAresta("a26", "23", "22")
        self.g_grande_bfs23.adicionaAresta("a27", "22", "21")
        self.g_grande_bfs23.adicionaAresta("a28", "21", "20")
        self.g_grande_bfs23.adicionaAresta("a29", "20", "19")
        self.g_grande_bfs23.adicionaAresta("a30", "19", "17")
        self.g_grande_bfs23.adicionaAresta("a31", "17", "16")
        self.g_grande_bfs23.adicionaAresta("a33", "18", "19")
        self.g_grande_bfs23.adicionaAresta("a34", "20", "10")

        # Grafos com ciclo
        self.com = MeuGrafo(["1", "2", "3", "4"])
        self.com.adicionaAresta("a1", "1", "2")
        self.com.adicionaAresta("a2", "1", "3")
        self.com.adicionaAresta("a3", "2", "4")
        self.com.adicionaAresta("a4", "3", "4")

        self.com2 = MeuGrafo(["1", "2"])
        self.com2.adicionaAresta("a1", "1", "2")
        self.com2.adicionaAresta("a2", "1", "2")

        self.com3 = MeuGrafo(["1"])
        self.com3.adicionaAresta("a1", "1", "1")

        # Grafos sem ciclo
        self.sem = MeuGrafo(["1", "2", "3", "4", "5"])
        self.sem.adicionaAresta("a1", "1", "2")
        self.sem.adicionaAresta("a2", "1", "3")
        self.sem.adicionaAresta("a3", "3", "4")
        self.sem.adicionaAresta("a4", "3", "5")

        # Grafos para teste de caminho euleriano
        self.slays = MeuGrafo(["a", "b", "c", "d", "e", "f", "g"])
        self.slays.adicionaAresta("a1", "a", "b")
        self.slays.adicionaAresta("a2", "a", "c")
        self.slays.adicionaAresta("a3", "a", "d")
        self.slays.adicionaAresta("a4", "a", "f")
        self.slays.adicionaAresta("a5", "b", "c")
        self.slays.adicionaAresta("a6", "b", "g")
        self.slays.adicionaAresta("a7", "b", "e")
        self.slays.adicionaAresta("a8", "e", "f")
        self.slays.adicionaAresta("a9", "f", "g")

        self.teste_conexo = MeuGrafo(["a", "b", "c", "d", "e", "f", "g", "h"])
        self.teste_conexo.adicionaAresta("a1", "a", "b")
        self.teste_conexo.adicionaAresta("a2", "a", "d")
        self.teste_conexo.adicionaAresta("a3", "b", "c")
        self.teste_conexo.adicionaAresta("a4", "c", "d")
        self.teste_conexo.adicionaAresta("a5", "d", "e")
        self.teste_conexo.adicionaAresta("a6", "e", "f")
        self.teste_conexo.adicionaAresta("a7", "e", "h")
        self.teste_conexo.adicionaAresta("a8", "f", "g")
        self.teste_conexo.adicionaAresta("a9", "g", "h")

        self.teste_desconexo = MeuGrafo(["a", "b", "c", "d", "e", "f", "g", "h"])
        self.teste_desconexo.adicionaAresta("a1", "a", "b")
        self.teste_desconexo.adicionaAresta("a2", "a", "d")
        self.teste_desconexo.adicionaAresta("a3", "b", "c")
        self.teste_desconexo.adicionaAresta("a4", "c", "d")
        self.teste_desconexo.adicionaAresta("a6", "e", "f")
        self.teste_desconexo.adicionaAresta("a7", "e", "h")
        self.teste_desconexo.adicionaAresta("a8", "f", "g")
        self.teste_desconexo.adicionaAresta("a9", "g", "h")

        self.pares = MeuGrafo(["a", "b", "c", "d", "e", "f"])
        self.pares.adicionaAresta("a1", "a", "b")
        self.pares.adicionaAresta("a2", "b", "c")
        self.pares.adicionaAresta("a3", "c", "d")
        self.pares.adicionaAresta("a4", "d", "e")
        self.pares.adicionaAresta("a5", "e", "f")
        self.pares.adicionaAresta("a6", "f", "a")

        # Grafos dos cursos do IFPB
        self.engenharia_de_computacao = MeuGrafo(
            [
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "31",
                "32",
                "33",
                "34",
                "35",
                "36",
                "41",
                "42",
                "43",
                "44",
                "45",
                "51",
                "52",
                "53",
                "54",
                "55",
                "61",
                "62",
                "63",
                "64",
                "65",
                "71",
                "72",
                "73",
                "74",
                "75",
                "81",
                "82",
                "83",
                "84",
                "85",
                "91",
                "92",
                "93",
                "94",
                "101",
                "102",
                "103",
            ]
        )
        self.engenharia_de_computacao.adicionaAresta("a1", "11", "21")
        self.engenharia_de_computacao.adicionaAresta("a2", "14", "24")
        self.engenharia_de_computacao.adicionaAresta("a3", "14", "25")
        self.engenharia_de_computacao.adicionaAresta("a4", "14", "34")
        self.engenharia_de_computacao.adicionaAresta("a5", "14", "35")
        self.engenharia_de_computacao.adicionaAresta("a6", "15", "24")
        self.engenharia_de_computacao.adicionaAresta("a7", "15", "25")
        self.engenharia_de_computacao.adicionaAresta("a8", "15", "34")
        self.engenharia_de_computacao.adicionaAresta("a9", "15", "35")
        self.engenharia_de_computacao.adicionaAresta("a10", "16", "26")
        self.engenharia_de_computacao.adicionaAresta("a11", "21", "31")
        self.engenharia_de_computacao.adicionaAresta("a12", "21", "41")
        self.engenharia_de_computacao.adicionaAresta("a13", "24", "33")
        self.engenharia_de_computacao.adicionaAresta("a14", "24", "43")
        self.engenharia_de_computacao.adicionaAresta("a15", "24", "44")
        self.engenharia_de_computacao.adicionaAresta("a16", "24", "53")
        self.engenharia_de_computacao.adicionaAresta("a17", "24", "54")
        self.engenharia_de_computacao.adicionaAresta("a18", "24", "72")
        self.engenharia_de_computacao.adicionaAresta("a19", "26", "36")
        self.engenharia_de_computacao.adicionaAresta("a20", "31", "51")
        self.engenharia_de_computacao.adicionaAresta("a21", "31", "52")
        self.engenharia_de_computacao.adicionaAresta("a22", "31", "64")
        self.engenharia_de_computacao.adicionaAresta("a23", "34", "63")
        self.engenharia_de_computacao.adicionaAresta("a24", "34", "81")
        self.engenharia_de_computacao.adicionaAresta("a25", "35", "63")
        self.engenharia_de_computacao.adicionaAresta("a26", "35", "81")
        self.engenharia_de_computacao.adicionaAresta("a27", "36", "44")
        self.engenharia_de_computacao.adicionaAresta("a28", "36", "45")
        self.engenharia_de_computacao.adicionaAresta("a29", "36", "55")
        self.engenharia_de_computacao.adicionaAresta("a30", "43", "62")
        self.engenharia_de_computacao.adicionaAresta("a31", "44", "55")
        self.engenharia_de_computacao.adicionaAresta("a32", "44", "93")
        self.engenharia_de_computacao.adicionaAresta("a33", "45", "93")
        self.engenharia_de_computacao.adicionaAresta("a34", "51", "61")
        self.engenharia_de_computacao.adicionaAresta("a35", "52", "75")
        self.engenharia_de_computacao.adicionaAresta("a36", "54", "81")
        self.engenharia_de_computacao.adicionaAresta("a37", "55", "65")
        self.engenharia_de_computacao.adicionaAresta("a38", "61", "84")
        self.engenharia_de_computacao.adicionaAresta("a39", "61", "94")
        self.engenharia_de_computacao.adicionaAresta("a40", "63", "73")
        self.engenharia_de_computacao.adicionaAresta("a41", "64", "75")
        self.engenharia_de_computacao.adicionaAresta("a42", "64", "84")
        self.engenharia_de_computacao.adicionaAresta("a43", "73", "82")
        self.engenharia_de_computacao.adicionaAresta("a44", "74", "83")
        self.engenharia_de_computacao.adicionaAresta("a45", "75", "85")
        self.engenharia_de_computacao.adicionaAresta("a46", "83", "92")
        self.engenharia_de_computacao.adicionaAresta("a47", "92", "103")

        self.construcao_de_edificios = MeuGrafo(
            [
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "31",
                "32",
                "33",
                "34",
                "35",
                "36",
                "37",
                "38",
                "41",
                "42",
                "43",
                "44",
                "45",
                "46",
                "47",
                "51",
                "52",
                "53",
                "54",
                "55",
                "56",
                "57",
                "58",
                "61",
                "62",
                "63",
                "64",
                "65",
                "66",
                "67",
                "68",
                "71",
                "72",
                "73",
            ]
        )
        self.construcao_de_edificios.adicionaAresta("a1", "11", "24")
        self.construcao_de_edificios.adicionaAresta("a2", "11", "35")
        self.construcao_de_edificios.adicionaAresta("a3", "11", "47")
        self.construcao_de_edificios.adicionaAresta("a4", "14", "23")
        self.construcao_de_edificios.adicionaAresta("a5", "15", "21")
        self.construcao_de_edificios.adicionaAresta("a6", "15", "25")
        self.construcao_de_edificios.adicionaAresta("a7", "15", "32")
        self.construcao_de_edificios.adicionaAresta("a8", "15", "34")
        self.construcao_de_edificios.adicionaAresta("a9", "17", "24")
        self.construcao_de_edificios.adicionaAresta("a10", "17", "26")
        self.construcao_de_edificios.adicionaAresta("a11", "17", "27")
        self.construcao_de_edificios.adicionaAresta("a12", "17", "41")
        self.construcao_de_edificios.adicionaAresta("a13", "17", "42")
        self.construcao_de_edificios.adicionaAresta("a14", "17", "46")
        self.construcao_de_edificios.adicionaAresta("a15", "17", "53")
        self.construcao_de_edificios.adicionaAresta("a16", "17", "55")
        self.construcao_de_edificios.adicionaAresta("a17", "21", "32")
        self.construcao_de_edificios.adicionaAresta("a18", "21", "33")
        self.construcao_de_edificios.adicionaAresta("a19", "21", "41")
        self.construcao_de_edificios.adicionaAresta("a20", "21", "42")
        self.construcao_de_edificios.adicionaAresta("a21", "22", "64")
        self.construcao_de_edificios.adicionaAresta("a22", "22", "66")
        self.construcao_de_edificios.adicionaAresta("a23", "23", "37")
        self.construcao_de_edificios.adicionaAresta("a24", "23", "43")
        self.construcao_de_edificios.adicionaAresta("a25", "24", "38")
        self.construcao_de_edificios.adicionaAresta("a26", "24", "44")
        self.construcao_de_edificios.adicionaAresta("a27", "25", "33")
        self.construcao_de_edificios.adicionaAresta("a28", "26", "36")
        self.construcao_de_edificios.adicionaAresta("a29", "27", "35")
        self.construcao_de_edificios.adicionaAresta("a30", "27", "64")
        self.construcao_de_edificios.adicionaAresta("a31", "31", "62")
        self.construcao_de_edificios.adicionaAresta("a32", "31", "67")
        self.construcao_de_edificios.adicionaAresta("a54", "32", "46")
        self.construcao_de_edificios.adicionaAresta("a33", "32", "53")
        self.construcao_de_edificios.adicionaAresta("a34", "32", "55")
        self.construcao_de_edificios.adicionaAresta("a35", "33", "64")
        self.construcao_de_edificios.adicionaAresta("a36", "35", "45")
        self.construcao_de_edificios.adicionaAresta("a37", "36", "45")
        self.construcao_de_edificios.adicionaAresta("a38", "36", "64")
        self.construcao_de_edificios.adicionaAresta("a39", "37", "45")
        self.construcao_de_edificios.adicionaAresta("a40", "37", "47")
        self.construcao_de_edificios.adicionaAresta("a41", "37", "51")
        self.construcao_de_edificios.adicionaAresta("a42", "41", "52")
        self.construcao_de_edificios.adicionaAresta("a43", "42", "52")
        self.construcao_de_edificios.adicionaAresta("a44", "43", "51")
        self.construcao_de_edificios.adicionaAresta("a45", "43", "57")
        self.construcao_de_edificios.adicionaAresta("a46", "44", "62")
        self.construcao_de_edificios.adicionaAresta("a47", "45", "51")
        self.construcao_de_edificios.adicionaAresta("a48", "45", "52")
        self.construcao_de_edificios.adicionaAresta("a49", "46", "51")
        self.construcao_de_edificios.adicionaAresta("a50", "46", "52")
        self.construcao_de_edificios.adicionaAresta("a51", "46", "56")
        self.construcao_de_edificios.adicionaAresta("a52", "47", "54")
        self.construcao_de_edificios.adicionaAresta("a53", "47", "65")

        self.fisica = MeuGrafo(
            [
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "31",
                "32",
                "33",
                "34",
                "35",
                "36",
                "37",
                "41",
                "42",
                "43",
                "44",
                "45",
                "46",
                "51",
                "52",
                "53",
                "54",
                "55",
                "56",
                "61",
                "62",
                "63",
                "64",
                "65",
                "66",
                "71",
                "72",
                "73",
                "74",
                "81",
                "82",
                "83",
                "84",
                "85",
            ]
        )
        self.fisica.adicionaAresta("a1", "11", "21")
        self.fisica.adicionaAresta("a2", "11", "22")
        self.fisica.adicionaAresta("a3", "12", "21")
        self.fisica.adicionaAresta("a4", "12", "22")
        self.fisica.adicionaAresta("a5", "12", "23")
        self.fisica.adicionaAresta("a6", "12", "24")
        self.fisica.adicionaAresta("a7", "14", "24")
        self.fisica.adicionaAresta("a8", "15", "25")
        self.fisica.adicionaAresta("a9", "16", "85")
        self.fisica.adicionaAresta("a10", "21", "31")
        self.fisica.adicionaAresta("a11", "21", "32")
        self.fisica.adicionaAresta("a12", "22", "32")
        self.fisica.adicionaAresta("a13", "23", "33")
        self.fisica.adicionaAresta("a14", "25", "85")
        self.fisica.adicionaAresta("a15", "31", "41")
        self.fisica.adicionaAresta("a16", "31", "42")
        self.fisica.adicionaAresta("a17", "31", "46")
        self.fisica.adicionaAresta("a18", "31", "54")
        self.fisica.adicionaAresta("a19", "31", "74")
        self.fisica.adicionaAresta("a20", "32", "42")
        self.fisica.adicionaAresta("a21", "33", "45")
        self.fisica.adicionaAresta("a22", "41", "51")
        self.fisica.adicionaAresta("a23", "41", "52")
        self.fisica.adicionaAresta("a24", "41", "72")
        self.fisica.adicionaAresta("a25", "42", "52")
        self.fisica.adicionaAresta("a26", "43", "55")
        self.fisica.adicionaAresta("a27", "43", "74")
        self.fisica.adicionaAresta("a28", "45", "51")
        self.fisica.adicionaAresta("a29", "45", "53")
        self.fisica.adicionaAresta("a30", "45", "72")
        self.fisica.adicionaAresta("a31", "51", "61")
        self.fisica.adicionaAresta("a32", "51", "62")
        self.fisica.adicionaAresta("a33", "51", "64")
        self.fisica.adicionaAresta("a34", "52", "62")
        self.fisica.adicionaAresta("a35", "53", "63")
        self.fisica.adicionaAresta("a36", "56", "66")
        self.fisica.adicionaAresta("a37", "61", "71")
        self.fisica.adicionaAresta("a38", "65", "81")
        self.fisica.adicionaAresta("a39", "66", "73")
        self.fisica.adicionaAresta("a40", "71", "84")
        self.fisica.adicionaAresta("a41", "73", "83")
        self.fisica.adicionaAresta("a42", "74", "82")

        self.matematica = MeuGrafo(
            [
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "21",
                "22",
                "23",
                "24",
                "25",
                "31",
                "32",
                "33",
                "34",
                "35",
                "36",
                "41",
                "42",
                "45",
                "44",
                "45",
                "46",
                "47",
                "51",
                "52",
                "53",
                "54",
                "55",
                "56",
                "57",
                "61",
                "62",
                "63",
                "64",
                "65",
                "67",
                "71",
                "72",
                "73",
                "74",
                "75",
                "77",
            ]
        )
        self.matematica.adicionaAresta("a1", "12", "21")
        self.matematica.adicionaAresta("a2", "13", "21")
        self.matematica.adicionaAresta("a3", "13", "23")
        self.matematica.adicionaAresta("a4", "16", "36")
        self.matematica.adicionaAresta("a5", "21", "31")
        self.matematica.adicionaAresta("a6", "21", "32")
        self.matematica.adicionaAresta("a7", "21", "52")
        self.matematica.adicionaAresta("a8", "22", "32")
        self.matematica.adicionaAresta("a9", "22", "42")
        self.matematica.adicionaAresta("a10", "22", "52")
        self.matematica.adicionaAresta("a11", "23", "33")
        self.matematica.adicionaAresta("a12", "24", "34")
        self.matematica.adicionaAresta("a13", "25", "35")
        self.matematica.adicionaAresta("a14", "31", "41")
        self.matematica.adicionaAresta("a15", "32", "42")
        self.matematica.adicionaAresta("a16", "33", "53")
        self.matematica.adicionaAresta("a17", "34", "44")
        self.matematica.adicionaAresta("a18", "36", "45")
        self.matematica.adicionaAresta("a19", "41", "62")
        self.matematica.adicionaAresta("a20", "41", "71")
        self.matematica.adicionaAresta("a21", "41", "72")
        self.matematica.adicionaAresta("a22", "45", "55")
        self.matematica.adicionaAresta("a23", "46", "56")
        self.matematica.adicionaAresta("a24", "47", "57")
        self.matematica.adicionaAresta("a25", "51", "61")
        self.matematica.adicionaAresta("a33", "55", "65")
        self.matematica.adicionaAresta("a26", "56", "64")
        self.matematica.adicionaAresta("a27", "56", "73")
        self.matematica.adicionaAresta("a28", "57", "67")
        self.matematica.adicionaAresta("a29", "64", "73")
        self.matematica.adicionaAresta("a30", "64", "74")
        self.matematica.adicionaAresta("a31", "65", "75")
        self.matematica.adicionaAresta("a32", "67", "77")

        self.telematica = MeuGrafo(
            [
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "31",
                "32",
                "33",
                "34",
                "35",
                "36",
                "37",
                "41",
                "42",
                "43",
                "44",
                "45",
                "46",
                "47",
                "51",
                "52",
                "53",
                "54",
                "55",
                "56",
                "61",
                "62",
                "63",
                "64",
                "65",
            ]
        )
        self.telematica.adicionaAresta("a1", "11", "21")
        self.telematica.adicionaAresta("a2", "12", "22")
        self.telematica.adicionaAresta("a3", "12", "23")
        self.telematica.adicionaAresta("a4", "13", "24")
        self.telematica.adicionaAresta("a5", "14", "34")
        self.telematica.adicionaAresta("a6", "16", "26")
        self.telematica.adicionaAresta("a7", "21", "31")
        self.telematica.adicionaAresta("a8", "21", "36")
        self.telematica.adicionaAresta("a9", "21", "46")
        self.telematica.adicionaAresta("a10", "22", "33")
        self.telematica.adicionaAresta("a11", "23", "33")
        self.telematica.adicionaAresta("a12", "24", "36")
        self.telematica.adicionaAresta("a13", "25", "35")
        self.telematica.adicionaAresta("a14", "26", "32")
        self.telematica.adicionaAresta("a15", "31", "41")
        self.telematica.adicionaAresta("a16", "31", "42")
        self.telematica.adicionaAresta("a17", "32", "43")
        self.telematica.adicionaAresta("a18", "32", "44")
        self.telematica.adicionaAresta("a19", "33", "44")
        self.telematica.adicionaAresta("a20", "33", "45")
        self.telematica.adicionaAresta("a21", "34", "46")
        self.telematica.adicionaAresta("a22", "37", "55")
        self.telematica.adicionaAresta("a23", "41", "51")
        self.telematica.adicionaAresta("a24", "41", "52")
        self.telematica.adicionaAresta("a25", "41", "55")
        self.telematica.adicionaAresta("a26", "42", "61")
        self.telematica.adicionaAresta("a27", "44", "53")
        self.telematica.adicionaAresta("a28", "44", "54")
        self.telematica.adicionaAresta("a29", "44", "55")
        self.telematica.adicionaAresta("a30", "51", "61")
        self.telematica.adicionaAresta("a31", "53", "62")

        self.letras = MeuGrafo(
            [
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "31",
                "32",
                "33",
                "34",
                "35",
                "36",
                "37",
                "41",
                "42",
                "43",
                "44",
                "45",
                "46",
                "47",
                "51",
                "52",
                "53",
                "54",
                "55",
                "56",
                "57",
                "61",
                "62",
                "63",
                "64",
                "65",
                "66",
                "67",
                "68",
                "71",
                "72",
                "73",
                "74",
                "75",
                "76",
                "77",
                "78",
                "79",
                "81",
                "82",
                "83",
                "84",
                "85",
                "86",
                "87",
                "88",
            ]
        )
        self.letras.adicionaAresta("a1", "11", "21")
        self.letras.adicionaAresta("a2", "11", "22")
        self.letras.adicionaAresta("a3", "12", "23")
        self.letras.adicionaAresta("a4", "12", "25")
        self.letras.adicionaAresta("a5", "13", "53")
        self.letras.adicionaAresta("a6", "17", "26")
        self.letras.adicionaAresta("a7", "17", "83")
        self.letras.adicionaAresta("a8", "21", "31")
        self.letras.adicionaAresta("a9", "21", "32")
        self.letras.adicionaAresta("a46", "21", "33")
        self.letras.adicionaAresta("a10", "22", "56")
        self.letras.adicionaAresta("a11", "23", "46")
        self.letras.adicionaAresta("a12", "24", "34")
        self.letras.adicionaAresta("a13", "25", "35")
        self.letras.adicionaAresta("a14", "25", "43")
        self.letras.adicionaAresta("a15", "25", "44")
        self.letras.adicionaAresta("a16", "27", "77")
        self.letras.adicionaAresta("a17", "31", "41")
        self.letras.adicionaAresta("a18", "31", "51")
        self.letras.adicionaAresta("a19", "31", "61")
        self.letras.adicionaAresta("a20", "31", "62")
        self.letras.adicionaAresta("a21", "31", "71")
        self.letras.adicionaAresta("a22", "31", "72")
        self.letras.adicionaAresta("a23", "31", "73")
        self.letras.adicionaAresta("a24", "33", "42")
        self.letras.adicionaAresta("a25", "35", "46")
        self.letras.adicionaAresta("a26", "35", "52")
        self.letras.adicionaAresta("a27", "35", "55")
        self.letras.adicionaAresta("a28", "35", "63")
        self.letras.adicionaAresta("a29", "35", "75")
        self.letras.adicionaAresta("a30", "37", "47")
        self.letras.adicionaAresta("a31", "37", "57")
        self.letras.adicionaAresta("a32", "37", "67")
        self.letras.adicionaAresta("a33", "45", "54")
        self.letras.adicionaAresta("a34", "45", "76")
        self.letras.adicionaAresta("a35", "53", "77")
        self.letras.adicionaAresta("a36", "54", "64")
        self.letras.adicionaAresta("a37", "54", "68")
        self.letras.adicionaAresta("a38", "64", "74")
        self.letras.adicionaAresta("a39", "64", "78")
        self.letras.adicionaAresta("a40", "65", "79")
        self.letras.adicionaAresta("a41", "68", "78")
        self.letras.adicionaAresta("a42", "74", "84")
        self.letras.adicionaAresta("a43", "74", "88")
        self.letras.adicionaAresta("a44", "77", "87")
        self.letras.adicionaAresta("a45", "78", "88")

        # Listas para análise topográfica
        self.engenharia_de_computacao_topografia = [
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "22",
            "23",
            "27",
            "32",
            "42",
            "71",
            "74",
            "91",
            "101",
            "102",
            "21",
            "24",
            "25",
            "26",
            "34",
            "35",
            "83",
            "31",
            "33",
            "36",
            "41",
            "43",
            "53",
            "54",
            "63",
            "72",
            "92",
            "44",
            "45",
            "51",
            "52",
            "62",
            "64",
            "73",
            "81",
            "103",
            "55",
            "61",
            "75",
            "82",
            "93",
            "65",
            "84",
            "85",
            "94",
        ]
        self.construcao_de_edificios_topografia = [
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "22",
            "31",
            "58",
            "61",
            "63",
            "68",
            "71",
            "72",
            "73",
            "21",
            "23",
            "24",
            "25",
            "26",
            "27",
            "34",
            "66",
            "67",
            "32",
            "33",
            "35",
            "36",
            "37",
            "38",
            "41",
            "42",
            "43",
            "44",
            "45",
            "46",
            "47",
            "53",
            "55",
            "57",
            "62",
            "64",
            "51",
            "52",
            "54",
            "56",
            "65",
        ]
        self.fisica_topografia = [
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "26",
            "27",
            "34",
            "35",
            "36",
            "37",
            "43",
            "44",
            "56",
            "65",
            "21",
            "22",
            "23",
            "24",
            "25",
            "55",
            "66",
            "81",
            "31",
            "32",
            "33",
            "73",
            "85",
            "41",
            "42",
            "45",
            "46",
            "54",
            "74",
            "83",
            "51",
            "52",
            "53",
            "72",
            "82",
            "61",
            "62",
            "63",
            "64",
            "71",
            "84",
        ]
        self.matematica_topografia = [
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "22",
            "24",
            "25",
            "46",
            "47",
            "51",
            "54",
            "63",
            "21",
            "23",
            "34",
            "35",
            "36",
            "56",
            "57",
            "61",
            "31",
            "32",
            "33",
            "44",
            "45",
            "45",
            "52",
            "64",
            "67",
            "41",
            "42",
            "53",
            "55",
            "73",
            "74",
            "77",
            "62",
            "65",
            "71",
            "72",
            "75",
        ]
        self.telematica_topografia = [
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "25",
            "27",
            "37",
            "47",
            "56",
            "63",
            "64",
            "65",
            "21",
            "22",
            "23",
            "24",
            "26",
            "34",
            "35",
            "31",
            "32",
            "33",
            "36",
            "46",
            "41",
            "42",
            "43",
            "44",
            "45",
            "51",
            "52",
            "53",
            "54",
            "55",
            "61",
            "62",
        ]
        self.letras_topografia = [
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "24",
            "27",
            "36",
            "37",
            "45",
            "65",
            "66",
            "81",
            "82",
            "85",
            "86",
            "21",
            "22",
            "23",
            "25",
            "26",
            "34",
            "47",
            "53",
            "54",
            "57",
            "67",
            "76",
            "79",
            "83",
            "31",
            "32",
            "33",
            "35",
            "43",
            "44",
            "56",
            "64",
            "68",
            "77",
            "41",
            "42",
            "46",
            "51",
            "52",
            "55",
            "61",
            "62",
            "63",
            "71",
            "72",
            "73",
            "74",
            "75",
            "78",
            "87",
            "84",
            "88",
        ]

    def test_warshall(self):
        with self.assertRaises(grafo_exceptions.VerticeInvalidoException):
            self.assertTrue(self.g_p.existe_caminho("J", "H"))
        with self.assertRaises(grafo_exceptions.VerticeInvalidoException):
            self.assertTrue(self.g_medio.existe_caminho("11", "1"))
        self.assertTrue(self.pares.existe_caminho("a", "a"))
        self.assertTrue(self.teste_conexo.existe_caminho("a", "e"))
        self.assertTrue(self.g_pequeno.existe_caminho("1", "5"))
        self.assertTrue(self.g_grande.existe_caminho("27", "5"))
        self.assertTrue(self.g_grande.existe_caminho("20", "16"))
        self.assertFalse(self.teste_desconexo.existe_caminho("a", "e"))
        self.assertFalse(self.slays.existe_caminho("d", "g"))
        self.assertFalse(self.g_medio.existe_caminho("10", "1"))

    def test_topografia(self):
        self.assertEqual(
            self.engenharia_de_computacao.topografia(),
            self.engenharia_de_computacao_topografia,
        )
        self.assertEqual(
            self.construcao_de_edificios.topografia(),
            self.construcao_de_edificios_topografia,
        )
        self.assertEqual(self.fisica.topografia(), self.fisica_topografia)
        self.assertEqual(self.matematica.topografia(), self.matematica_topografia)
        self.assertEqual(self.telematica.topografia(), self.telematica_topografia)
        self.assertEqual(self.letras.topografia(), self.letras_topografia)

if __name__ == "__main__":
    unittest.main()
