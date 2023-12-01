class Graph:
    """
        ESTRUTURA DE DADOS GRAFO
        É uma estrutura de dados não-linear, formada por vértices
        (ou nodos, ou nós) e arestas (ou arcos). Sua principal
        finalidade é representar as relações entre diferentes
        entidades. Tais relações podem ser bidirecionais, resultando
        em grafos não direcionados, ou unidirecionais, constituindo
        grafos direcionados (digrafos). Entre suas aplicações, estão
        representações de redes de computadores, mapas, caminhos e
        redes sociais.
    """
    def __init__(self, is_directed = False):
        """ Método construtor """
        self.__is_directed = is_directed    # O grafo é direcionado?

        # __data__ armazenará o grafo no formato de LISTA DE ADJACÊNCIA
        self.__data = {}    # Dicionário vazio
        # print("GRAFO:", self.__data)

    def add_vertex(self, val):
        """
            Método que adiciona um vértice ao grafo
        """
        # Verifica se o vértice já existe no dicionário.
        # A criação só ocorre se o vértice ainda não existir
        if not val in self.__data:
            self.__data[val] = set()    # Conjunto vazio
        # print("GRAFO:", self.__data)

    def add_edge(self, origin, dest, label = None):
        """
            Método que adiciona uma aresta entre dois vértices
            origin: vértice de origem
            dest: vértice de destino
            label: rótulo descritivo do relacionamento (opcional)
        """
        # Cria os vértices de origem e destino, caso ainda não existam
        if not origin in self.__data: self.add_vertex(origin)
        if not dest in self.__data: self.add_vertex(dest)

        # Monta a aresta
        edge1 = (dest, label)   # Isto é uma tupla ("lista imutável")

        # Adiciona a aresta origem -> destino
        self.__data[origin].add(edge1)

        # Se o grafo não for direcionado, devemos adicionar também
        # uma aresta no sentido oposto, isto é, destino -> origem
        if not self.__is_directed:
            edge2 = (origin, label)     # Tupla
            self.__data[dest].add(edge2)

        # print("GRAFO:", self.__data)

    def __get_degree(self, vertex):
        """
            Método que retorna o grau (número de vértices que entram ou saem)
            de um vértice
        """
        total = 0
        # GRAU DE SAÍDA (OUT-DEGREE)
        # É determinado contando-se o número de arestas associadas à
        # entrada de dicionário correspondente ao vértice
        if vertex in self.__data: total = len(self.__data[vertex])

        # GRAU DE ENTRADA (IN-DEGREE)
        # É determinado procurando-se referências ao vértice nas arestas
        # associadas a cada um dos vértices do dicionário
        for v in self.__data.keys():    # Percorre o dicionário (vértices)
            for e in self.__data[v]:    # Percorre os conjuntos (arestas)
                if vertex == e[0]: total += 1

        # O grau final é a soma dos graus de entrada e saída
        return total
    
    def remove_edge(self, origin, dest, label = None):
        """
            Método que remove uma aresta do grafo, tendo sido fornecidos
            o vértice de origem, o vértice de destino e o rótulo (opcional)
        """
        edge1 = (dest, label)   # Montagem da aresta
        # Retira edge1 do conjunto de arestas do vértice de origem
        self.__data[origin].discard(edge1)

        # Se o grafo não for direcionado, precisamos remover também a aresta
        # em sentido contrário
        if not self.__is_directed:
            edge2 = (origin, label)
            self.__data[dest].discard(edge2)

        # print("GRAFO:", self.__data)

    def remove_vertex(self, vertex):
        """
            Método que exclui um vértice do grafo
            (Para que um vértice possa ser excluído, ele não pode ter arestas
            saindo ou entrando, ou seja, deve ter grau zero.)
        """
        if self.__get_degree(vertex) != 0:
            raise Exception("ERRO: impossível remover um vértice com grau diferente de zero.")
        
        if vertex in self.__data: del self.__data[vertex]   # Exclui o vértice

    def __str__(self):
        """
            Método que cria uma representação do grafo como string
        """
        output = str(self.__data)
        output += f"\nDirecionado? {self.__is_directed}\n\n"
        return output