from bibgrafo.grafo_matriz_adj_nao_dir import \
    GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        """
        Provê uma lista de vértices não adjacentes no grafo. A lista
        terá o seguinte formato: [X-Z, X-W, ...], onde X, Z e W são
        vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes.
        """
        vertices = []

        for i in range(len(self.M)):
            for j in range(i, len(self.M)):
                if not self.M[i][j] and i != j:
                    vertices.append(f'{self.N[i]}-{self.N[j]}')

        return vertices

    def ha_laco(self):
        """
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        """
        for i in range(len(self.M)):
            if len(self.M[i][i]) > 0:
                return True

        return False

    def grau(self, v):
        """
        Provê o grau do vértice passado como parâmetro.
        :param v: O rótulo do vértice a ser analisado.
        :return: Um valor inteiro que indica o grau do vértice.
        :raises VerticeInvalidoException: Caso o vértice não exista.
        """
        if v not in self.N:
            raise VerticeInvalidoException(f'O vértice {v} não é válido.')

        indice = self.N.index(v)
        grau = 0

        for i in range(indice, len(self.M)):
            if indice == i:
                grau += len(self.M[indice][i]) * 2
            else:
                grau += len(self.M[indice][i])

        for j in range(indice):
            grau += len(self.M[j][indice])

        return grau

    def ha_paralelas(self):
        """
        Verifica se há arestas paralelas no grafo.
        :return: Um valor booleano que indica se existem arestas
        paralelas no grafo.
        """
        for i in range(len(self.M)):
            for j in range(i, len(self.M)):
                if len(self.M[i][j]) >= 2:
                    return True

        return False

    def arestas_sobre_vertice(self, v):
        """
        Provê uma lista que contém os rótulos das arestas que incidem
        sobre o vértice passado como parâmetro.
        :param v: O vértice a ser analisado.
        :return: Uma lista os rótulos das arestas que incidem sobre o
        vértice.
        :raises VerticeInvalidoException: Caso o vértice não exista.
        """
        if v not in self.N:
            raise VerticeInvalidoException(f'O vértice {v} não existe.')

        indice = self.N.index(v)
        arestas = []

        for i in range(indice):
            arestas += list(self.M[i][indice].keys())

        for j in range(indice, len(self.M)):
            arestas += list(self.M[indice][j].keys())

        return arestas

    def eh_completo(self):
        """
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo.
        """
        if self.ha_laco() or self.ha_paralelas():
            return False

        for i in range(len(self.M) - 1):
            for j in range(i + 1, len(self.M)):
                if len(self.M[i][j]) != 1:
                    return False

        return True

    def _elevar_matriz(self, matriz, numero_de_vertices, resultado=None, contador=2):
        util = [[0 for _ in range(numero_de_vertices)] for _ in
                range(numero_de_vertices)]

        for i in range(numero_de_vertices):
            for j in range(i, numero_de_vertices):
                for k in range(numero_de_vertices):
                    if contador == 2:
                        util[i][j] += matriz[i][k] * matriz[k][j]
                    else:
                        util[i][j] += resultado[i][k] * matriz[k][j]

        if contador < numero_de_vertices:
            contador += 1
            util = self._elevar_matriz(matriz, numero_de_vertices, util, contador)

        return util

    def conexo(self):
        if len(self.M) == 1:
            return True

        numero_de_vertices = len(self.N)
        matriz = [[0 if i != j else 1 for i in range(numero_de_vertices)]
                  for j in range(numero_de_vertices)]

        for i in range(numero_de_vertices):
            for j in range(i, numero_de_vertices):
                if len(self.M[i][j]) > 0:
                    matriz[i][j] = 1

        resultado = self._elevar_matriz(matriz, numero_de_vertices)

        return False if 0 in resultado[0] else True

    def listar_arestas(self):
        chaves = []
        valores = []

        for i in range(len(self.M)):
            for j in range(i, len(self.M)):
                if self.M[i][j]:
                    chaves += list(self.M[i][j].keys())
                    valores += list(self.M[i][j].values())

        arestas = {}
        for indice, chave in enumerate(chaves):
            arestas[chave] = valores[indice]

        return arestas

    def _caminho_util(self, raiz, matriz, caminho):
        indice = self.N.index(raiz)
        vizinhos = []

        for i in range(indice):
            if len(self.M[i][indice]) >= 1:
                vizinhos.append(self.N[i])

        for j in range(indice, len(self.M)):
            if len(self.M[indice][j]) >= 1:
                vizinhos.append(self.N[j])

        if not vizinhos:
            print('terminou')
            return
        elif len(vizinhos) == 1:
            caminho += [raiz]
            arestas = matriz.listar_arestas()

            for rotulo in arestas:
                v1 = arestas[rotulo].getV1()
                v2 = arestas[rotulo].getV2()

                if (v1 or v2) == raiz and (v1 or v2) == vizinhos[0]:
                    caminho += [rotulo, vizinhos[0]]
                    self._caminho_util(vizinhos[0], matriz, caminho)

        return vizinhos

    def caminho_euleriano(self):
        vertices_impares = 0
        vertices_iniciais = []

        for vertice in self.N:
            if self.grau(vertice) % 2 != 0:
                vertices_impares += 1
                vertices_iniciais.append(vertice)

            if vertices_impares > 2:
                return False

        if vertices_impares == 1 or not self.conexo():
            return False

        caminho = []
        print(self._caminho_util('f', self.M, caminho))
