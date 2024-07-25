class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #https://www.youtube.com/watch?v=aBxjDBC4M1U - nocely explained disjoined sets concept
        #we use ranks by which we know which is the ultimate parent of a given node, initially all the nodes are alone and have a rank one
        parent = [i for i in range(len(edges)+1)]
        rank = [1 for i in range(len(edges)+1)]
        def find(p):
            if p == parent[p]:
                return p
            return find(parent[p])
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]+rank[p2]
            else:
                parent[p1]=p2
                rank[p2]+=p1
            return True
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]