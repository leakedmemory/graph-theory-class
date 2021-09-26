# from meu_grafo import MeuGrafo
# from meu_grafo_matriz_adjacencia_nao_dir import MeuGrafo
from meu_grafo_matriz_adjacencia_dir import MeuGrafo

engenharia_de_computacao = MeuGrafo(
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
engenharia_de_computacao.adicionaAresta("a1", "11", "21")
engenharia_de_computacao.adicionaAresta("a2", "14", "24")
engenharia_de_computacao.adicionaAresta("a3", "14", "25")
engenharia_de_computacao.adicionaAresta("a4", "14", "34")
engenharia_de_computacao.adicionaAresta("a5", "14", "35")
engenharia_de_computacao.adicionaAresta("a6", "15", "24")
engenharia_de_computacao.adicionaAresta("a7", "15", "25")
engenharia_de_computacao.adicionaAresta("a8", "15", "34")
engenharia_de_computacao.adicionaAresta("a9", "15", "35")
engenharia_de_computacao.adicionaAresta("a10", "16", "26")
engenharia_de_computacao.adicionaAresta("a11", "21", "31")
engenharia_de_computacao.adicionaAresta("a12", "21", "41")
engenharia_de_computacao.adicionaAresta("a13", "24", "33")
engenharia_de_computacao.adicionaAresta("a14", "24", "43")
engenharia_de_computacao.adicionaAresta("a15", "24", "44")
engenharia_de_computacao.adicionaAresta("a16", "24", "53")
engenharia_de_computacao.adicionaAresta("a17", "24", "54")
engenharia_de_computacao.adicionaAresta("a18", "24", "72")
engenharia_de_computacao.adicionaAresta("a19", "26", "36")
engenharia_de_computacao.adicionaAresta("a20", "31", "51")
engenharia_de_computacao.adicionaAresta("a21", "31", "52")
engenharia_de_computacao.adicionaAresta("a22", "31", "64")
engenharia_de_computacao.adicionaAresta("a23", "34", "63")
engenharia_de_computacao.adicionaAresta("a24", "34", "81")
engenharia_de_computacao.adicionaAresta("a25", "35", "63")
engenharia_de_computacao.adicionaAresta("a26", "35", "81")
engenharia_de_computacao.adicionaAresta("a27", "36", "44")
engenharia_de_computacao.adicionaAresta("a28", "36", "45")
engenharia_de_computacao.adicionaAresta("a29", "36", "55")
engenharia_de_computacao.adicionaAresta("a30", "43", "62")
engenharia_de_computacao.adicionaAresta("a31", "44", "55")
engenharia_de_computacao.adicionaAresta("a32", "44", "93")
engenharia_de_computacao.adicionaAresta("a33", "45", "93")
engenharia_de_computacao.adicionaAresta("a34", "51", "61")
engenharia_de_computacao.adicionaAresta("a35", "52", "75")
engenharia_de_computacao.adicionaAresta("a36", "54", "81")
engenharia_de_computacao.adicionaAresta("a37", "55", "65")
engenharia_de_computacao.adicionaAresta("a38", "61", "84")
engenharia_de_computacao.adicionaAresta("a39", "61", "94")
engenharia_de_computacao.adicionaAresta("a40", "63", "73")
engenharia_de_computacao.adicionaAresta("a41", "64", "75")
engenharia_de_computacao.adicionaAresta("a42", "64", "84")
engenharia_de_computacao.adicionaAresta("a43", "73", "82")
engenharia_de_computacao.adicionaAresta("a44", "74", "83")
engenharia_de_computacao.adicionaAresta("a45", "75", "85")
engenharia_de_computacao.adicionaAresta("a46", "83", "92")
engenharia_de_computacao.adicionaAresta("a47", "92", "103")

construcao_de_edificios = MeuGrafo(
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
construcao_de_edificios.adicionaAresta("a1", "11", "24")
construcao_de_edificios.adicionaAresta("a2", "11", "35")
construcao_de_edificios.adicionaAresta("a3", "11", "47")
construcao_de_edificios.adicionaAresta("a4", "14", "23")
construcao_de_edificios.adicionaAresta("a5", "15", "21")
construcao_de_edificios.adicionaAresta("a6", "15", "25")
construcao_de_edificios.adicionaAresta("a7", "15", "32")
construcao_de_edificios.adicionaAresta("a8", "15", "34")
construcao_de_edificios.adicionaAresta("a9", "17", "24")
construcao_de_edificios.adicionaAresta("a10", "17", "26")
construcao_de_edificios.adicionaAresta("a11", "17", "27")
construcao_de_edificios.adicionaAresta("a12", "17", "41")
construcao_de_edificios.adicionaAresta("a13", "17", "42")
construcao_de_edificios.adicionaAresta("a14", "17", "46")
construcao_de_edificios.adicionaAresta("a15", "17", "53")
construcao_de_edificios.adicionaAresta("a16", "17", "55")
construcao_de_edificios.adicionaAresta("a17", "21", "32")
construcao_de_edificios.adicionaAresta("a18", "21", "33")
construcao_de_edificios.adicionaAresta("a19", "21", "41")
construcao_de_edificios.adicionaAresta("a20", "21", "42")
construcao_de_edificios.adicionaAresta("a21", "22", "64")
construcao_de_edificios.adicionaAresta("a22", "22", "66")
construcao_de_edificios.adicionaAresta("a23", "23", "37")
construcao_de_edificios.adicionaAresta("a24", "23", "43")
construcao_de_edificios.adicionaAresta("a25", "24", "38")
construcao_de_edificios.adicionaAresta("a26", "24", "44")
construcao_de_edificios.adicionaAresta("a27", "25", "33")
construcao_de_edificios.adicionaAresta("a28", "26", "36")
construcao_de_edificios.adicionaAresta("a29", "27", "35")
construcao_de_edificios.adicionaAresta("a30", "27", "64")
construcao_de_edificios.adicionaAresta("a31", "31", "62")
construcao_de_edificios.adicionaAresta("a32", "31", "67")
construcao_de_edificios.adicionaAresta("a54", "32", "46")
construcao_de_edificios.adicionaAresta("a33", "32", "53")
construcao_de_edificios.adicionaAresta("a34", "32", "55")
construcao_de_edificios.adicionaAresta("a35", "33", "64")
construcao_de_edificios.adicionaAresta("a36", "35", "45")
construcao_de_edificios.adicionaAresta("a37", "36", "45")
construcao_de_edificios.adicionaAresta("a38", "36", "64")
construcao_de_edificios.adicionaAresta("a39", "37", "45")
construcao_de_edificios.adicionaAresta("a40", "37", "47")
construcao_de_edificios.adicionaAresta("a41", "37", "51")
construcao_de_edificios.adicionaAresta("a42", "41", "52")
construcao_de_edificios.adicionaAresta("a43", "42", "52")
construcao_de_edificios.adicionaAresta("a44", "43", "51")
construcao_de_edificios.adicionaAresta("a45", "43", "57")
construcao_de_edificios.adicionaAresta("a46", "44", "62")
construcao_de_edificios.adicionaAresta("a47", "45", "51")
construcao_de_edificios.adicionaAresta("a48", "45", "52")
construcao_de_edificios.adicionaAresta("a49", "46", "51")
construcao_de_edificios.adicionaAresta("a50", "46", "52")
construcao_de_edificios.adicionaAresta("a51", "46", "56")
construcao_de_edificios.adicionaAresta("a52", "47", "54")
construcao_de_edificios.adicionaAresta("a53", "47", "65")

fisica = MeuGrafo(
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
fisica.adicionaAresta("a1", "11", "21")
fisica.adicionaAresta("a2", "11", "22")
fisica.adicionaAresta("a3", "12", "21")
fisica.adicionaAresta("a4", "12", "22")
fisica.adicionaAresta("a5", "12", "23")
fisica.adicionaAresta("a6", "12", "24")
fisica.adicionaAresta("a7", "14", "24")
fisica.adicionaAresta("a8", "15", "25")
fisica.adicionaAresta("a9", "16", "85")
fisica.adicionaAresta("a10", "21", "31")
fisica.adicionaAresta("a11", "21", "32")
fisica.adicionaAresta("a12", "22", "32")
fisica.adicionaAresta("a13", "23", "33")
fisica.adicionaAresta("a14", "25", "85")
fisica.adicionaAresta("a15", "31", "41")
fisica.adicionaAresta("a16", "31", "42")
fisica.adicionaAresta("a17", "31", "46")
fisica.adicionaAresta("a18", "31", "54")
fisica.adicionaAresta("a19", "31", "74")
fisica.adicionaAresta("a20", "32", "42")
fisica.adicionaAresta("a21", "33", "45")
fisica.adicionaAresta("a22", "41", "51")
fisica.adicionaAresta("a23", "41", "52")
fisica.adicionaAresta("a24", "41", "72")
fisica.adicionaAresta("a25", "42", "52")
fisica.adicionaAresta("a26", "43", "55")
fisica.adicionaAresta("a27", "43", "74")
fisica.adicionaAresta("a28", "45", "51")
fisica.adicionaAresta("a29", "45", "53")
fisica.adicionaAresta("a30", "45", "72")
fisica.adicionaAresta("a31", "51", "61")
fisica.adicionaAresta("a32", "51", "62")
fisica.adicionaAresta("a33", "51", "64")
fisica.adicionaAresta("a34", "52", "62")
fisica.adicionaAresta("a35", "53", "63")
fisica.adicionaAresta("a36", "56", "66")
fisica.adicionaAresta("a37", "61", "71")
fisica.adicionaAresta("a38", "65", "81")
fisica.adicionaAresta("a39", "66", "73")
fisica.adicionaAresta("a40", "71", "84")
fisica.adicionaAresta("a41", "73", "83")
fisica.adicionaAresta("a42", "74", "82")

matematica = MeuGrafo(
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
matematica.adicionaAresta("a1", "12", "21")
matematica.adicionaAresta("a2", "13", "21")
matematica.adicionaAresta("a3", "13", "23")
matematica.adicionaAresta("a4", "16", "36")
matematica.adicionaAresta("a5", "21", "31")
matematica.adicionaAresta("a6", "21", "32")
matematica.adicionaAresta("a7", "21", "52")
matematica.adicionaAresta("a8", "22", "32")
matematica.adicionaAresta("a9", "22", "42")
matematica.adicionaAresta("a10", "22", "52")
matematica.adicionaAresta("a11", "23", "33")
matematica.adicionaAresta("a12", "24", "34")
matematica.adicionaAresta("a13", "25", "35")
matematica.adicionaAresta("a14", "31", "41")
matematica.adicionaAresta("a15", "32", "42")
matematica.adicionaAresta("a16", "33", "53")
matematica.adicionaAresta("a17", "34", "44")
matematica.adicionaAresta("a18", "36", "45")
matematica.adicionaAresta("a19", "41", "62")
matematica.adicionaAresta("a20", "41", "71")
matematica.adicionaAresta("a21", "41", "72")
matematica.adicionaAresta("a22", "45", "55")
matematica.adicionaAresta("a23", "46", "56")
matematica.adicionaAresta("a24", "47", "57")
matematica.adicionaAresta("a25", "51", "61")
matematica.adicionaAresta("a33", "55", "65")
matematica.adicionaAresta("a26", "56", "64")
matematica.adicionaAresta("a27", "56", "73")
matematica.adicionaAresta("a28", "57", "67")
matematica.adicionaAresta("a29", "64", "73")
matematica.adicionaAresta("a30", "64", "74")
matematica.adicionaAresta("a31", "65", "75")
matematica.adicionaAresta("a32", "67", "77")

telematica = MeuGrafo(
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
telematica.adicionaAresta("a1", "11", "21")
telematica.adicionaAresta("a2", "12", "22")
telematica.adicionaAresta("a3", "12", "23")
telematica.adicionaAresta("a4", "13", "24")
telematica.adicionaAresta("a5", "14", "34")
telematica.adicionaAresta("a6", "16", "26")
telematica.adicionaAresta("a7", "21", "31")
telematica.adicionaAresta("a8", "21", "36")
telematica.adicionaAresta("a9", "21", "46")
telematica.adicionaAresta("a10", "22", "33")
telematica.adicionaAresta("a11", "23", "33")
telematica.adicionaAresta("a12", "24", "36")
telematica.adicionaAresta("a13", "25", "35")
telematica.adicionaAresta("a14", "26", "32")
telematica.adicionaAresta("a15", "31", "41")
telematica.adicionaAresta("a16", "31", "42")
telematica.adicionaAresta("a17", "32", "43")
telematica.adicionaAresta("a18", "32", "44")
telematica.adicionaAresta("a19", "33", "44")
telematica.adicionaAresta("a20", "33", "45")
telematica.adicionaAresta("a21", "34", "46")
telematica.adicionaAresta("a22", "37", "55")
telematica.adicionaAresta("a23", "41", "51")
telematica.adicionaAresta("a24", "41", "52")
telematica.adicionaAresta("a25", "41", "55")
telematica.adicionaAresta("a26", "42", "61")
telematica.adicionaAresta("a27", "44", "53")
telematica.adicionaAresta("a28", "44", "54")
telematica.adicionaAresta("a29", "44", "55")
telematica.adicionaAresta("a30", "51", "61")
telematica.adicionaAresta("a31", "53", "62")

letras = MeuGrafo(
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
letras.adicionaAresta("a1", "11", "21")
letras.adicionaAresta("a2", "11", "22")
letras.adicionaAresta("a3", "12", "23")
letras.adicionaAresta("a4", "12", "25")
letras.adicionaAresta("a5", "13", "53")
letras.adicionaAresta("a6", "17", "26")
letras.adicionaAresta("a7", "17", "83")
letras.adicionaAresta("a8", "21", "31")
letras.adicionaAresta("a9", "21", "32")
letras.adicionaAresta("a46", "21", "33")
letras.adicionaAresta("a10", "22", "56")
letras.adicionaAresta("a11", "23", "46")
letras.adicionaAresta("a12", "24", "34")
letras.adicionaAresta("a13", "25", "35")
letras.adicionaAresta("a14", "25", "43")
letras.adicionaAresta("a15", "25", "44")
letras.adicionaAresta("a16", "27", "77")
letras.adicionaAresta("a17", "31", "41")
letras.adicionaAresta("a18", "31", "51")
letras.adicionaAresta("a19", "31", "61")
letras.adicionaAresta("a20", "31", "62")
letras.adicionaAresta("a21", "31", "71")
letras.adicionaAresta("a22", "31", "72")
letras.adicionaAresta("a23", "31", "73")
letras.adicionaAresta("a24", "33", "42")
letras.adicionaAresta("a25", "35", "46")
letras.adicionaAresta("a26", "35", "52")
letras.adicionaAresta("a27", "35", "55")
letras.adicionaAresta("a28", "35", "63")
letras.adicionaAresta("a29", "35", "75")
letras.adicionaAresta("a30", "37", "47")
letras.adicionaAresta("a31", "37", "57")
letras.adicionaAresta("a32", "37", "67")
letras.adicionaAresta("a33", "45", "54")
letras.adicionaAresta("a34", "45", "76")
letras.adicionaAresta("a35", "53", "77")
letras.adicionaAresta("a36", "54", "64")
letras.adicionaAresta("a37", "54", "68")
letras.adicionaAresta("a38", "64", "74")
letras.adicionaAresta("a39", "64", "78")
letras.adicionaAresta("a40", "65", "79")
letras.adicionaAresta("a41", "68", "78")
letras.adicionaAresta("a42", "74", "84")
letras.adicionaAresta("a43", "74", "88")
letras.adicionaAresta("a44", "77", "87")
letras.adicionaAresta("a45", "78", "88")

print(letras.ordem_topologica())
