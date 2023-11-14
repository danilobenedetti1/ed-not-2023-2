from lib.graph import Graph

g = Graph()     # Grafo será não direcionado
print(g)

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("D")   # Duplicado de propósito
g.add_vertex("E")
print(g)

# Criação de uma aresta
g.add_edge("A", "B")
g.add_edge("A", "C")
print(g)

# Remoção de uma aresta
g.remove_edge("A", "B")
print(g)

##############################################

print("-" * 80)

familia = Graph(True)   # Grafo direcionado
print(familia)

familia.add_edge("Joaquim", "Fabíola", "PAI")
familia.add_edge("Fabíola", "Joaquim", "FILHA")
print(familia)

familia.remove_edge("Joaquim", "Fabíola", "PAI")
print(familia)