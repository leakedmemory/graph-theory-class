import copy
import math
import bibgrafo

from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo import grafo_exceptions


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
                    vertices.append(f"{self.N[i]}-{self.N[j]}")

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
            raise grafo_exceptions.VerticeInvalidoException(
                f"O vértice {v} não é válido."
            )

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

    def rotulos_sobre_vertice(self, v):
        """
        Provê uma lista que contém os rótulos das arestas que incidem
        sobre o vértice passado como parâmetro.
        :param v: O vértice a ser analisado.
        :return: Uma lista com os rótulos das arestas que incidem sobre
        o vértice.
        :raises VerticeInvalidoException: Caso o vértice não exista.
        """
        if v not in self.N:
            raise grafo_exceptions.VerticeInvalidoException(
                f"O vértice {v} não existe."
            )

        indice = self.N.index(v)
        arestas = []

        for i in range(indice):
            arestas += list(self.M[i][indice].keys())

        for j in range(indice, len(self.M)):
            arestas += list(self.M[indice][j].keys())

        return arestas

    def arestas_sobre_vertice(self, v):
        """
        Provê uma lista que contém os rótulos das arestas que incidem
        sobre o vértice passado como parâmetro.
        :param v: O vértice a ser analisado.
        :return: Uma lista com os objetos aresta que incidem sobre o
        vértice.
        :raises VerticeInvalidoException: Caso o vértice não exista.
        """
        if v not in self.N:
            raise grafo_exceptions.VerticeInvalidoException(
                f"O vértice {v} não existe."
            )

        indice = self.N.index(v)
        arestas = []

        for i in range(indice):
            arestas += list(self.M[i][indice].values())

        for j in range(indice, len(self.M)):
            arestas += list(self.M[indice][j].values())

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
        """
        Função recursiva auxiliar utilizada para saber se o grafo é
        conexo. A recursividade é parada quando o número de vértices é
        igual ao expoente da matriz.
        :param matriz: Matriz contendo 1 na diagonal principal e nos
        locais em que há aresta entre i e j.
        :param numero_de_vertices: Número de vértices presentes no grafo.
        :param resultado: Parâmetro para salvar o resultado obtido na
        multiplicação feita anteriormente.
        :param contador: Parâmetro para salvar a que grau a matriz já
        foi elevada.
        :return: Retorna matriz^numero_de_vertices.
        """
        util = [
            [0 for _ in range(numero_de_vertices)] for _ in range(numero_de_vertices)
        ]

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
        """
        Testa se o grafo é conexo.
        :return: Valor booleano, sendo True para grafo conexo.
        """
        if len(self.M) == 1:
            return True

        numero_de_vertices = len(self.N)
        matriz = [
            [0 if i != j else 1 for i in range(numero_de_vertices)]
            for j in range(numero_de_vertices)
        ]

        for i in range(numero_de_vertices):
            for j in range(numero_de_vertices):
                if len(self.M[i][j]) > 0 and self.M[i][j] != "-":
                    matriz[i][j] = matriz[j][i] = 1

        resultado = self._elevar_matriz(matriz, numero_de_vertices)

        for i in range(len(resultado) - 1):
            if 0 not in resultado[i]:
                return True

        return False

    def remove_aresta(self, rotulo, vertice):
        """
        Remove uma aresta do grafo. Caso o grau do vértice raiz se torne
        0 após a remoção, esse vértice será excluído do grafo.
        :param rotulo: Rótulo da aresta a ser removida.
        :param vertice: Vértice que, caso se torne de grau 0, será removido.
        :return: None
        """
        if rotulo not in self.listar_arestas():
            raise grafo_exceptions.ArestaInvalidaException(
                f"A aresta {rotulo} não existe."
            )

        for i in range(len(self.M)):
            for j in range(i, len(self.M)):
                if rotulo in self.M[i][j]:
                    del self.M[i][j][rotulo]
                    break

        if self.grau(vertice) == 0:
            indice = self.N.index(vertice)
            del self.M[indice]

            for row in range(len(self.M)):
                del self.M[row][indice]

            del self.N[indice]

    def listar_arestas(self):
        """
        Lista as arestas presentes no grafo.
        :return: Dicionário no formato {rótulo: objeto aresta}.
        """
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

    def _caminho_util(self, raiz, matriz, caminho=None):
        """
        Função recursiva utilizada para formar o caminho euleriano.
        :param raiz: Vértice raiz inicial.
        :param matriz: Cópia do grafo matriz adjacência.
        :param caminho: Caminho euleriano a ser formado.
        :return: Parâmetro caminho com o caminho completo.
        """
        if caminho is None:
            caminho = []
        indice = matriz.N.index(raiz)
        vizinhos = []

        for i in range(indice):
            if len(matriz.M[i][indice]) >= 1:
                vizinhos.append(matriz.N[i])

        for j in range(indice, len(matriz.M)):
            if len(matriz.M[indice][j]) >= 1:
                vizinhos.append(matriz.N[j])

        if not vizinhos:
            caminho += [raiz]
            return caminho
        else:
            arestas = matriz.listar_arestas()

            for rotulo in arestas:
                v1 = arestas[rotulo].getV1()
                v2 = arestas[rotulo].getV2()

                for vizinho in vizinhos:
                    if v1 == raiz and v2 == vizinho or v1 == vizinho and v2 == raiz:
                        if len(vizinhos) == 1:
                            caminho += [raiz, rotulo]
                            matriz.remove_aresta(rotulo, raiz)
                            self._caminho_util(vizinhos[0], matriz, caminho)

                            if len(matriz.N) == 1:
                                return caminho
                        else:
                            teste = copy.deepcopy(matriz)
                            teste.remove_aresta(rotulo, raiz)

                            if teste.conexo():
                                caminho += [raiz, rotulo]
                                matriz.remove_aresta(rotulo, raiz)
                                self._caminho_util(vizinho, matriz, caminho)

                                if len(matriz.N) == 1:
                                    return caminho

    def caminho_euleriano(self):
        """
        Tenta montar um caminho euleriano com base no grafo.
        :return: Retorna uma lista do caminho percorrido no seguinte
        formato: [vértice, aresta, vértice, aresta, ..., vértice]. Caso
        não haja um caminho euleriano, retorna o booleano False.
        """
        if len(self.N) == 1 and not self.listar_arestas():
            return False
        elif len(self.N) == 1 and len(self.listar_arestas().keys()) == 1:
            return [self.N[0], list(self.listar_arestas().keys())[0], self.N[0]]
        elif len(self.N) == 1 and len(self.listar_arestas().keys()) > 1:
            return False

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

        if vertices_iniciais:
            for vertice in vertices_iniciais:
                copia = copy.deepcopy(self)
                caminho = self._caminho_util(vertice, copia)

                if not copia.listar_arestas():
                    return caminho
        else:
            for vertice in self.N:
                copia = copy.deepcopy(self)
                caminho = self._caminho_util(vertice, copia)

                if not copia.listar_arestas():
                    return caminho

    def vertice_com_menor_aresta(self):
        dicionario = {v: math.inf for v in self.N}

        for i in range(len(self.M)):
            for j in range(i, len(self.M)):
                objetos = list(self.M[i][j].values())
                for objeto in objetos:
                    rotulo = objeto.getV1()
                    if objeto.getPeso() < dicionario[rotulo]:
                        dicionario[rotulo] = objeto.getPeso()

        return sorted(dicionario.items(), key=lambda x: x[1])[0][0]

    @staticmethod
    def _is_vertice(v1, v2, vertice):
        return v1 == vertice or v2 == vertice

    def aresta_menor_peso_em_vertice(self, vertice):
        arestas = self.listar_arestas()
        menor_aresta = None
        menor_rotulo = ""

        for rotulo, aresta in arestas.items():
            v1 = aresta.getV1()
            v2 = aresta.getV2()

            if self._is_vertice(v1, v2, vertice) and (
                menor_aresta is None or menor_aresta.getPeso() > aresta.getPeso()
            ):
                menor_aresta = aresta
                menor_rotulo = rotulo

        return menor_rotulo, menor_aresta

    def _menor_aresta(self, vertices):
        d = {}

        for vertice in vertices:
            a, b = self.aresta_menor_peso_em_vertice(vertice)
            if b is not None:
                d[a] = b

        return sorted(d.items(), key=lambda x: x[1].getPeso())[0]

    def prim(self):
        if not self.conexo():
            raise grafo_exceptions.MatrizInvalidaException(
                f"O grafo matriz adjacência não é conexo."
            )

        tree = MeuGrafo(self.N.copy())
        copia = copy.deepcopy(self)
        v_visitados = [copia.vertice_com_menor_aresta()]
        v_nao_visitados = tree.N.copy()
        v_nao_visitados.remove(v_visitados[0])

        while v_nao_visitados:
            rotulo, aresta = copia._menor_aresta(v_visitados)

            tree.adicionaAresta(
                aresta.getRotulo(),
                aresta.getV1(),
                aresta.getV2(),
                aresta.getPeso(),
            )

            if aresta.getV1() in v_visitados and aresta.getV2() not in v_visitados:
                v_nao_visitados.remove(aresta.getV2())
                v_visitados.append(aresta.getV2())
                copia.remove_aresta(rotulo, aresta.getV2())
            elif aresta.getV2() in v_visitados and aresta.getV1() not in v_visitados:
                v_nao_visitados.remove(aresta.getV1())
                v_visitados.append(aresta.getV1())
                copia.remove_aresta(rotulo, aresta.getV1())
            else:
                copia.remove_aresta(rotulo, aresta.getV1())

        return tree
