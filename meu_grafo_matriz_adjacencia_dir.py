import copy

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

    def _remover_linha_do_vertice(self, indice):
        self.M.pop(indice)

    def _remover_coluna_do_vertice(self, indice):
        for linha in range(len(self.M)):
            self.M[linha].pop(indice)

    def remover_vertice(self, vertice):
        indice = self.N.index(vertice)
        self._remover_linha_do_vertice(indice)
        self._remover_coluna_do_vertice(indice)
        self.N.pop(indice)

    def _ha_saida_no_vertice(self, vertice):
        indice = self.N.index(vertice)
        for i in range(len(self.N)):
            if self.M[indice][i]:
                return True

        return False

    def _ha_entrada_no_vertice(self, vertice):
        indice = self.N.index(vertice)
        for i in range(len(self.N)):
            if self.M[i][indice]:
                return True

        return False

    def _e_grau_0(self, vertice):
        if self._ha_entrada_no_vertice(vertice) or self._ha_saida_no_vertice(vertice):
            return False

        return True

    def _listar_vertices_grau_0(self):
        vertices_grau_0 = []
        for vertice in self.N:
            if self._e_grau_0(vertice):
                vertices_grau_0.append(vertice)

        return vertices_grau_0

    def _listar_vertices_apenas_saida(self):
        vertices_apenas_saida = []
        for vertice in self.N:
            if self._ha_saida_no_vertice(vertice) and not self._ha_entrada_no_vertice(
                vertice
            ):
                vertices_apenas_saida.append(vertice)

        return vertices_apenas_saida

    def topografia(self):
        grafo = copy.deepcopy(self)
        topografia = []

        while True:
            vertices_grau_0 = grafo._listar_vertices_grau_0()
            vertices_apenas_saida = grafo._listar_vertices_apenas_saida()
            vertices_vistos = sorted(
                vertices_grau_0 + vertices_apenas_saida, key=lambda x: int(x)
            )
            if not vertices_vistos:
                return topografia

            topografia += vertices_vistos
            for vertice in vertices_vistos:
                grafo.remover_vertice(vertice)
