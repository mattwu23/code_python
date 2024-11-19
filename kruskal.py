#Kruskal's Algorithm

#Sort the Edges by Weight
#Add the Smallest Edge if it Doesn’t Make a Loop
#Repeat Until All Points Are Connected
edges = [
    (1, 'A', 'B'),
    (4, 'B', 'C'),
    (3, 'A', 'C'),
    (2, 'B', 'D'),
    (5, 'C', 'D')
]
# Union-Find with a simple dictionary
parent = {}

def find(point):
    if parent[point] != point:
        parent[point] = find(parent[point])
    return parent[point]

def union(p1, p2):
    root1 = find(p1)
    root2 = find(p2)
    if root1 != root2:
        parent[root2] = root1

def kruskal(edges):
    mst = []
    # Initialize parent pointers
    for weight, u, v in edges:
        parent[u] = u
        parent[v] = v

    # Sort edges by weight
    edges.sort()

    for weight, u, v in edges:
        if find(u) != find(v):  # Check for loops
            union(u, v)
            mst.append((weight, u, v))

    return mst

mst = kruskal(edges)
print("Minimum Spanning Tree:", mst)