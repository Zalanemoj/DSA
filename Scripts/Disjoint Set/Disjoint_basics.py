class DisjointSet:
    def __init__(self,nodes:int):
        self.parent=[i for i in range(0,nodes+1)]
        self.rank=[0]*(nodes+1)

    def find_parent(self,node:int) -> int:
        if node==self.parent[node]:
            return node

        self.parent[node]=self.find_parent(self.parent[node])

        return self.parent[node]

    def union(self,u:int,v:int):
        parent_u=self.find_parent(u)
        parent_v=self.find_parent(v)

        if parent_u==parent_v:
            return

        if self.rank[parent_u]<self.rank[parent_v]:
            self.parent[parent_u]=parent_v
        elif self.rank[parent_u]>self.rank[parent_v]:
            self.parent[parent_v]=parent_u
        else:
            self.parent[parent_v]=parent_u
            self.rank[parent_u]+=1

ds=DisjointSet(7)
ds.union(1,2)
ds.union(2,3)
ds.union(4,5)
ds.union(6,7)
ds.union(5,6)
ds.union(3,7)

print(ds.find_parent(5))
print(ds.find_parent(6))
print(ds.find_parent(7))
print(ds.find_parent(4))
print(ds.find_parent(1))