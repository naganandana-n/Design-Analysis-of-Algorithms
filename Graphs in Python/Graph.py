'''
GRAPHS (https://www.youtube.com/watch?v=VTH21EqzECk)
------

- VERTEX / NODE : REPRESENTED IN A MATRIX
- EDGE : CONNECTION B/W NODES, BIDIRECTIONAL, REPRESENTED IN A MATRIX (ADJACENCY LIST / MATRIX)
'''

# REPRESENTING A GRAPH (IN IMAGE - Graphs)

graph = {
    'a' : ['b', 'c'],
    'b' : ['a', 'd'],
    'c' : ['a', 'd'],
    'd' : ['b', 'c', 'e'],
    'e' : ['d']
}

# PRINTING OUT VERTICES

vertices = graph.keys()
print("\n")
print("VERTICES: ")
print(vertices)
print("\n")

# PRINTING OUT EDGES

edges = []
for vertex in graph:
    for item in graph[vertex]:
        if {vertex, item} not in edges: # PREVENTS EDGES FROM BEING REPEATED (EG, AB & BA)
            edges.append({vertex, item})

print("EDGES: ")
print(edges)
print("\n")

