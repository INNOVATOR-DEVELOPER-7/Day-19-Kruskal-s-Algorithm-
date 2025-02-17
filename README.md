# Day-19-Kruskal-s-Algorithm-
Here's Python Program for Kruskal's Algorithm. Day 19 of Day 365.
- Initial Setup: Start with a weighted, connected, and undirected graph, represented as nodes (vertices) and edges with weights. Sort all the edges in non-decreasing order of their weights.
- Initialize Sets: Create a subset for each vertex, each containing only that vertex.
- Edge Selection: Select the smallest edge and check if it forms a cycle with the spanning tree formed so far. If it doesn’t form a cycle, include it in the MST (Minimum Spanning Tree).
- Union of Sets: If the edge is included in the MST, perform a union of the sets containing the two vertices of the edge.
- Repeat: Continue the process until there are ( V-1 ) edges in the MST, where ( V ) is the number of vertices.

Example:
Graph:

```
    (1)       (3)
  A ----- B ------ C
    \    |      /
  (3)\    |    /(1)
      \   |   /
       v  v  /
        D - E
       (2)
```

Edges:
- (A, B) = 1
- (A, D) = 3
- (B, C) = 3
- (B, E) = 3
- (C, E) = 1
- (D, E) = 2

Sorted Edges: (A, B), (C, E), (D, E), (A, D), (B, C), (B, E)

1. Initial MST: [ ]
2. Edge Selection:
   - Select (A, B), include in MST (no cycle)
   - MST: [(A, B)]
3. Edge Selection:
   - Select (C, E), include in MST (no cycle)
   - MST: [(A, B), (C, E)]
4. Edge Selection:
   - Select (D, E), include in MST (no cycle)
   - MST: [(A, B), (C, E), (D, E)]
5. Edge Selection:
   - Select (A, D), include in MST (no cycle)
   - MST: [(A, B), (C, E), (D, E), (A, D)]
6. Edge Selection:
   - Ignore (B, C) (forms a cycle)
   - Ignore (B, E) (forms a cycle)

Final MST:
- Edges: (A, B), (C, E), (D, E), (A, D)
- Total weight: 1 + 1 + 2 + 3 = 7
