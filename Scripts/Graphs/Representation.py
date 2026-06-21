# Variables that are given in the questions like a number of nodes edges and the interconnection between them.
No_Nodes=5
No_Edges=6

Edges=[[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]]

# Storing graphs in a matrix.
matrix=[[0 for _ in range(No_Nodes+1)] for _ in range(No_Edges+1)]

for u,v in Edges:
    matrix[u][v]=1
    matrix[v][u]=1

print(matrix)

# Storing graph in a list.
lst=[[] for _ in range(No_Nodes+1)]

for u,v in Edges:
    lst[u].append(v)
    lst[v].append(u)

print(lst)