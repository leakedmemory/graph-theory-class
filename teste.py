# from meu_grafo import MeuGrafo
from meu_grafo_matriz_adjacencia_nao_dir import MeuGrafo

# from meu_grafo_matriz_adjacencia_dir import MeuGrafo

peso3 = MeuGrafo(
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
peso3.adicionaAresta("a1", "1", "2", 4)
peso3.adicionaAresta("a2", "2", "3", 3)
peso3.adicionaAresta("a3", "1", "4", 9)
peso3.adicionaAresta("a4", "3", "4", 5)
peso3.adicionaAresta("a5", "3", "5", 14)
peso3.adicionaAresta("a6", "3", "8", 6)
peso3.adicionaAresta("a7", "8", "12", 4)
peso3.adicionaAresta("a8", "8", "9", 15)
peso3.adicionaAresta("a9", "8", "11", 11)
peso3.adicionaAresta("a10", "12", "13", 13)
peso3.adicionaAresta("a11", "13", "14", 13)
peso3.adicionaAresta("a12", "14", "16", 8)
peso3.adicionaAresta("a13", "14", "15", 3)
peso3.adicionaAresta("a14", "4", "6", 6)
peso3.adicionaAresta("a15", "6", "30", 2)
peso3.adicionaAresta("a16", "30", "29", 14)
peso3.adicionaAresta("a17", "29", "28", 2)
peso3.adicionaAresta("a18", "28", "25", 12)
peso3.adicionaAresta("a19", "28", "27", 2)
peso3.adicionaAresta("a20", "27", "26", 5)
peso3.adicionaAresta("a21", "26", "25", 12)
peso3.adicionaAresta("a22", "25", "23", 8)
peso3.adicionaAresta("a23", "23", "24", 4)
peso3.adicionaAresta("a24", "23", "7", 3)
peso3.adicionaAresta("a25", "7", "5", 7)
peso3.adicionaAresta("a26", "23", "22", 2)
peso3.adicionaAresta("a27", "22", "21", 15)
peso3.adicionaAresta("a28", "21", "20", 11)
peso3.adicionaAresta("a29", "20", "19", 6)
peso3.adicionaAresta("a30", "19", "17", 8)
peso3.adicionaAresta("a31", "17", "16", 9)
peso3.adicionaAresta("a32", "17", "18", 11)
peso3.adicionaAresta("a33", "18", "19", 8)
peso3.adicionaAresta("a34", "20", "10", 12)
peso3.adicionaAresta("a35", "10", "9", 2)
peso3.adicionaAresta("a36", "10", "11", 9)

teste = MeuGrafo(["a", "b", "c", "d", "e", "f", "g", "h"])
teste.adicionaAresta("a1", "a", "b", 9)
teste.adicionaAresta("a2", "a", "g", 4)
teste.adicionaAresta("a3", "b", "c", 6)
teste.adicionaAresta("a4", "b", "g", 10)
teste.adicionaAresta("a5", "b", "h", 7)
teste.adicionaAresta("a6", "c", "d", 8)
teste.adicionaAresta("a7", "c", "e", 12)
teste.adicionaAresta("a8", "d", "e", 14)
teste.adicionaAresta("a9", "e", "f", 2)
teste.adicionaAresta("a10", "f", "g", 1)
teste.adicionaAresta("a11", "f", "h", 2)

pares = MeuGrafo(["a", "b", "c", "d", "e", "f"])
pares.adicionaAresta("a1", "a", "b", 4)
pares.adicionaAresta("a2", "a", "f", 5)
pares.adicionaAresta("a3", "b", "c", 2)
pares.adicionaAresta("a4", "c", "d", 3)
pares.adicionaAresta("a5", "d", "e", 7)
pares.adicionaAresta("a6", "e", "f", 9)

# print(peso3.prim())
print(peso3.kruskal())
