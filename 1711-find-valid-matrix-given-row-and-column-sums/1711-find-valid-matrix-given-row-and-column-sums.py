class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        #https://www.youtube.com/watch?v=Ks6fGnXkHPg
        n = len(rowSum)
        m = len(colSum)
        mat = [[0] * m for _ in range(n)] 
        for i in range(n):
            mat[i][0]=rowSum[i]
        for c in range(m):
            curCol = 0
            for r in range(n):
                curCol+=mat[r][c]
            r = 0
            while curCol>colSum[c]:
                diff = curCol - colSum[c]
                max_shift = min(mat[r][c],diff)
                mat[r][c]-=max_shift
                mat[r][c+1]+=max_shift
                curCol-=max_shift
                r+=1
        
        return mat