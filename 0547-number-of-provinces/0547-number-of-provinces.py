class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #solved using union find method
        n = len(isConnected)
        m = len(isConnected[0])
        parent = [i for i in range (n)]
        rank = [1]*n
        
        def find(p):
            while p!=parent[p]:
                parent[p] = parent[parent[p]] #path compression
                p = parent[p]
            return p

        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1==p2:
                return 0
            else:
                if rank[p1]>rank[p2]:
                    rank[p1]+=rank[p2]
                    parent[p2]=p1
                else:
                    rank[p2]+=rank[p1]
                    parent[p1]=p2
            return 1
        edges = []
        
        for i in range(n):
            for j in range(m):
                if isConnected[i][j]==1 and i!=j:
                    edges.append([i,j])
        res = n #no of nodes

        for n1,n2 in edges:
            res-=union(n1,n2)#subtract no of times we do union
        return res
