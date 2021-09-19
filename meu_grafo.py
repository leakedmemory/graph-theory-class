from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo import grafo_exceptions


class MeuGrafo(GrafoListaAdjacencia):
    def _listar_com_rotulo(self):
        """
        Produz com uma lista das arestas do grafo no seguinte formato:
        [(A, a1, B)].
        :return: Lista das arestas de maneira rotulada.
        """
        vertices_adjacentes = []

        for a in self.A:
            aresta_atual = self.A[a]
            v1 = aresta_atual.getV1()
            v2 = aresta_atual.getV2()

            if v1 not in vertices_adjacentes:
                vertices_adjacentes.append((v1, a, v2))

        return vertices_adjacentes

    def _dfs_util(self, raiz, dfs, percorridos, adjacentes):
        """
        Produz o caminho percorrido na busca em profundidade de maneira
        recursiva.
        :param raiz: Vértice raiz por onde se deseja começar a busca.
        :param dfs: Objeto MeuGrafo final onde será colocado as arestas.
        :param percorridos: Lista dos vértices percorridos.
        :param adjacentes: Lista dos vértices adjacentes.
        :return: Parâmetro dfs completo.
        """
        percorridos += [raiz]
        rotulos = []

        for aresta in adjacentes:
            if aresta[0] == raiz:
                rotulos.append(aresta)
            elif aresta[-1] == raiz:
                rotulos.append((aresta[-1], aresta[1], aresta[0]))

        for aresta in rotulos:
            if aresta[-1] not in percorridos:
                dfs.adicionaAresta(aresta[1], aresta[0], aresta[-1])
                self._dfs_util(aresta[-1], dfs, percorridos, adjacentes)

    def _dfs_ciclo(self, raiz, dicionario, v_percorridos, a_percorridas, adjacentes):
        v_percorridos += [raiz]
        rotulos = []

        for aresta in adjacentes:
            if aresta[0] == raiz:
                rotulos.append(aresta)
            elif aresta[-1] == raiz:
                rotulos.append((aresta[-1], aresta[1], aresta[0]))

        for aresta in rotulos:
            if aresta[-1] not in v_percorridos:
                a_percorridas += [aresta[1]]
                dicionario[aresta[-1]] = raiz
                self._dfs_ciclo(
                    aresta[-1], dicionario, v_percorridos, a_percorridas, adjacentes
                )
            elif aresta[-1] == v_percorridos[0] and aresta[1] not in a_percorridas:
                dicionario[aresta[-1]] = raiz
                return

    def _montar_ciclo(self, dicionario, caminho, chave, a_percorridas):
        if len(caminho) == 0:
            caminho += [chave]
        elif len(caminho) >= 3 and caminho[0] == caminho[-1]:
            return caminho

        for a in self.A:
            v1 = self.A[a].getV1()
            v2 = self.A[a].getV2()

            if v1 == chave and v2 == dicionario[chave] and a not in a_percorridas:
                a_percorridas += [a]
                caminho += [a, v2]
                self._montar_ciclo(dicionario, caminho, v2, a_percorridas)
            elif v1 == dicionario[chave] and v2 == chave and a not in a_percorridas:
                a_percorridas += [a]
                caminho += [a, v1]
                self._montar_ciclo(dicionario, caminho, v1, a_percorridas)

    def _dfs_maior(self, raiz, v_percorridos, distancias):
        adjacentes = self._listar_com_rotulo()
        rotulos = []

        for aresta in adjacentes:
            if aresta[0] == raiz:
                rotulos.append(aresta)
            elif aresta[-1] == raiz:
                rotulos.append((aresta[-1], aresta[1], aresta[0]))

        for aresta in rotulos:
            if aresta[-1] not in v_percorridos:
                v_percorridos += [aresta[-1]]
                distancias[aresta[-1]] = distancias[raiz] + 1
                self._dfs_maior(aresta[-1], v_percorridos, distancias)

    def _dfs_caminho(self, raiz, v_percorridos, caminho):
        vertice = None
        aresta_melhor = None
        profundidade = -1

        adjacentes = self._listar_com_rotulo()
        rotulos = []

        for aresta in adjacentes:
            if aresta[0] == raiz:
                rotulos.append(aresta)
            elif aresta[-1] == raiz:
                rotulos.append((aresta[-1], aresta[1], aresta[0]))

        for aresta in rotulos:
            if aresta[-1] not in v_percorridos:
                copia = v_percorridos.copy() + [aresta[-1]]
                distancias = {aresta[-1]: 0}
                self._dfs_maior(aresta[-1], copia, distancias)

                tmp = max(list(distancias.values()))
                if tmp > profundidade:
                    profundidade = tmp
                    aresta_melhor = aresta[1]
                    vertice = aresta[-1]

        if profundidade != -1:
            v_percorridos += [vertice]
            caminho += [aresta_melhor, vertice]
            self._dfs_caminho(vertice, v_percorridos, caminho)

    def vertices_adjacentes(self, vertice):
        """
        Mostra quais são os vértices adjacentes do vértice informado.
        :param vertice: Vértice que se deseja ver os adjacentes.
        :return: Lista ordenada dos vértices adjacentes do vértice dado.
        """
        adjacentes = set()

        for a in self.A:
            if self.A[a].getV1() == vertice:
                adjacentes.add(self.A[a].getV2())
            elif self.A[a].getV2() == vertice:
                adjacentes.add(self.A[a].getV1())

        return sorted(list(adjacentes))

    def dicionario(self):
        """
        Produz um dicionário do grafo; maneira comumente usada para
        representação.
        :return: Dicionário representante do grafo.
        """
        dicionario = {c: [] for c in self.N}

        for n in self.N:
            for a in self.A:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()

                if v1 == n and n not in dicionario[v2]:
                    dicionario[n].append(v2)
                elif v2 == n and n not in dicionario[v1]:
                    dicionario[n].append(v1)

        return dicionario

    def vertices_nao_adjacentes(self):
        """
        Provê uma lista de vértices não adjacentes no grafo. A lista
        terá o formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre
        eles.
        :return: Uma lista com os pares de vértices não adjacentes
        """
        tmp = {c: [] for c in self.N}
        nao_adjacentes = []

        for n in self.N:
            adjacentes = self.vertices_adjacentes(n)
            filtered = sorted(list(filter(lambda x: x != n, self.N)))

            for d in adjacentes:
                filtered.remove(d)

            for e in filtered:
                if e not in tmp[n] and n not in tmp[e]:
                    tmp[n].append(e)

        for key in tmp.keys():
            for v in tmp[key]:
                nao_adjacentes.append(f"{key}-{v}")

        return nao_adjacentes

    def ha_laco(self):
        """
        Verifica se existe algum laço no grafo.
        :return: Valor booleano que indica se existe algum laço.
        """
        for a in self.A:
            if self.A[a].getV1() == self.A[a].getV2():
                return True

        return False

    def grau(self, vertice):
        """
        Provê o grau do vértice passado como parâmetro.
        :param vertice: O rótulo do vértice a ser analisado.
        :return: Um valor inteiro que indica o grau do vértice.
        :raises VerticeInvalidoException: Caso o vértice passado não
        exista no grafo.
        """
        if vertice not in self.N:
            raise grafo_exceptions.VerticeInvalidoException

        grau = 0

        for a in self.A:
            if self.A[a].getV1() == vertice and self.A[a].getV2() == vertice:
                grau += 2
            elif self.A[a].getV1() == vertice or self.A[a].getV2() == vertice:
                grau += 1

        return grau

    def ha_paralelas(self):
        """
        Verifica se há arestas paralelas no grafo.
        :return: Um valor booleano que indica se existem arestas
        paralelas no grafo.
        """
        combinacoes = []

        for a in self.A:
            aresta = f"{self.A[a].getV1()}-{self.A[a].getV2()}"

            if aresta in combinacoes:
                return True

            combinacoes.append(aresta)

        return False

    def arestas_sobre_vertice(self, vertice):
        """
        Provê uma lista que contém os rótulos das arestas que incidem
        sobre o vértice passado como parâmetro.
        :param vertice: O vértice a ser analisado.
        :return: Uma lista os rótulos das arestas que incidem sobre o
        vértice.
        :raise VerticeInvalidoException: Caso o vértice passado não
        exista no grafo.
        """
        if vertice not in self.N:
            raise grafo_exceptions.VerticeInvalidoException(
                f"O vértice {vertice} é inválido."
            )

        arestas = []

        for a in self.A:
            if self.A[a].getV1() == vertice or self.A[a].getV2() == vertice:
                arestas.append(a)

        return arestas

    def eh_completo(self):
        """
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        """
        if self.ha_laco() or self.ha_paralelas():
            return False

        for n in self.N:
            adjacentes = self.vertices_adjacentes(n)
            tmp = sorted(list(filter(lambda x: x != n, self.N)))

            if adjacentes != tmp:
                return False

        return True

    def dfs(self, raiz):
        """
        Faz uma busca em profundidade.
        :param raiz: Vértice raiz onde se inicia a busca.
        :return: Objeto MeuGrafo resultante da busca.
        :raise VerticeInvalidoException: Caso o vértice raiz passado não
        existir no grafo.
        """
        if raiz not in self.N:
            raise grafo_exceptions.VerticeInvalidoException(
                f"O vértice {raiz} é inválido."
            )

        dfs = MeuGrafo(self.N)

        adjacentes = self._listar_com_rotulo()
        percorridos = []

        self._dfs_util(raiz, dfs, percorridos, adjacentes)

        return dfs

    def bfs(self, raiz):
        """
        Faz uma busca em largura no grafo a partir do vértice dado.
        :param raiz: Vértice raiz onde se inicia a busca.
        :return: Objeto MeuGrafo com o resultado da busca.
        :raise VerticeInvalidoException: Caso o vértice raiz passado não
        existir no grafo.
        """
        if raiz not in self.N:
            raise grafo_exceptions.VerticeInvalidoException(
                f"O vértice {raiz} é inválido."
            )

        bfs = MeuGrafo([raiz])
        visitados = [raiz]
        fila = [raiz]

        while fila:
            for a in self.A:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                visto = fila[0]

                if v1 == visto or v2 == visto:
                    if visto == v1:
                        adjacente = v2
                    else:
                        adjacente = v1

                    if not bfs.existeVertice(v1):
                        bfs.adicionaVertice(v1)
                    if not bfs.existeVertice(v2):
                        bfs.adicionaVertice(v2)

                    if adjacente not in visitados:
                        fila.append(adjacente)
                        visitados.append(adjacente)
                        bfs.adicionaAresta(a, visto, adjacente)

            fila.pop(0)

        return bfs

    def ha_clico(self):
        """
        Realiza uma busca em profundidade para verificar se há ciclos no
        grafo.
        :return: Uma lista com o caminho do primeiro ciclo encontrado ou
        False se não encontrar nenhum ciclo.
        """
        adjacentes = self._listar_com_rotulo()

        for n in self.N:
            dicionario = {n: None}
            v_percorridos = []
            a_percorridas = []
            self._dfs_ciclo(n, dicionario, v_percorridos, a_percorridas, adjacentes)

            chaves = list(dicionario.keys())
            if dicionario[chaves[0]] is None and n == self.N[-1]:
                return False
            elif dicionario[chaves[0]] is not None:
                caminho = []
                arestas = []
                self._montar_ciclo(dicionario, caminho, chaves[0], arestas)

                return caminho

    def caminho(self, tamanho):
        if tamanho > len(self.A) or tamanho >= len(self.N):
            return False

        for n in self.N:
            v_percorridos = [n]
            caminho = [n]
            self._dfs_caminho(n, v_percorridos, caminho)

            if tamanho <= len(caminho[1::2]):
                return caminho[: 2 * tamanho + 1]

        return False

    def conexo(self):
        """
        Realiza uma busca em largura afim de saber se o grafo é conexo
        ou não.
        :return: Valor booleano dizendo se o grafo é conexo.
        """
        bfs = self.bfs(self.N[0])
        if len(self.N) == len(bfs.N):
            return True

        return False
