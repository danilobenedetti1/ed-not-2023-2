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
        print("GRAFO:", self.__data)

    def add_vertex(self, val):
        """
            Método que adiciona um vértice ao grafo
        """
        # Verifica se o vértice já existe no dicionário.
        # A criação só ocorre se o vértice ainda não existir
        if not val in self.__data:
            self.__data[val] = set()    # Conjunto vazio
        print("GRAFO:", self.__data)

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

        print("GRAFO:", self.__data)