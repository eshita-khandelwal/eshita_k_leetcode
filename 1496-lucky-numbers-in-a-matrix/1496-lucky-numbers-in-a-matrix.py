class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = []
        col =[]
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            min1=float('inf')
            for j in range(m):
                if matrix[i][j]<min1:
                    min1=matrix[i][j]

            row.append(min1)
        for i in range(m):
            max1=float('-inf')
            for j in range(n):
                if matrix[j][i]>max1:
                    max1=matrix[j][i]

            col.append(max1)
        happy=[]
        for i in range(n):
            for j in range(m):
                if row[i]==matrix[i][j] and col[j]==matrix[i][j]:
                    happy.append(matrix[i][j])
        
        return happy

        
