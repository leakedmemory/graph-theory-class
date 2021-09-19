from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from bibgrafo import grafo_exceptions


class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):
    def existe_caminho(self, raiz, destino):
        """
        Utiliza o algoritmo de Warshall para verificar se há uma caminho
        entre os vértices passados nos parâmetros.
        :param raiz: Vértice de onde parte a busca.
        :param destino: Vértice onde se deseja chegar.
        :return: Valor booleano que representa a existência desse
        caminho.
        """
        if raiz not in self.N:
            raise grafo_exceptions.VerticeInvalidoException(
                f"O vértice {raiz} não é válido."
            )
        elif destino not in self.N:
            raise grafo_exceptions.VerticeInvalidoException(
                f"O vértice {destino} não é válido."
            )

        indice_raiz = self.N.index(raiz)
        indice_destino = self.N.index(destino)
        if self.M[indice_raiz][indice_destino]:
            return True

        matrix = [
            [
                1 if self.M[i][j] and self.M[i][j] != "-" else 0
                for j in range(len(self.M))
            ]
            for i in range(len(self.M))
        ]

        numero_de_vertices = len(self.N)

        for i in range(numero_de_vertices):
            for j in range(numero_de_vertices):
                if matrix[j][i] == 1:
                    for k in range(numero_de_vertices):
                        matrix[j][k] = max(matrix[j][k], matrix[i][k])

                        if matrix[indice_raiz][indice_destino]:
                            return True

        return False
