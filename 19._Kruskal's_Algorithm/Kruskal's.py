class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(graph, vertices):
    mst = []
    disjoint_set = DisjointSet(vertices)
    edges = sorted(graph, key=lambda edge: edge[2])

    for edge in edges:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append(edge)

    return mst

# Get the number of vertices from the user
num_vertices = int(input("Enter the number of vertices: "))
vertices = []
for i in range(num_vertices):
    vertex = input(f"Enter the name of vertex {i+1}: ")
    vertices.append(vertex)

# Get the edges of the graph from the user
num_edges = int(input("Enter the number of edges: "))
graph = []
print("Enter each edge in the format 'source destination weight':")
for i in range(num_edges):
    edge = input().split()
    graph.append((edge[0], edge[1], int(edge[2])))

# Perform Kruskal's algorithm
mst = kruskal(graph, vertices)

# Print the Minimum Spanning Tree (MST)
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"({u}, {v}) with weight {weight}")
