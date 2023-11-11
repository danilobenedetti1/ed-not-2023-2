from lib.graph import Graph

g = Graph()     # Grafo será não direcionado

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("D")   # Duplicado de propósito
g.add_vertex("E")

# Criação de uma aresta
g.add_edge("A", "B")
g.add_edge("A", "C")

##############################################

print("-" * 80)

familia = Graph(True)   # Grafo direcionado

familia.add_edge("Joaquim", "Fabíola", "PAI")
familia.add_edge("Fabíola", "Joaquim", "FILHA")