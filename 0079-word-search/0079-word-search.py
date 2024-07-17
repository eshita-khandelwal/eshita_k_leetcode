class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i,j,cnt):
            if cnt == len(word):
                return True
            if i<0 or i>=n or j<0 or j>=m or board[i][j]!=word[cnt]:
                return False
            temp = board[i][j]
            board[i][j]='0'
            cnt+=1
            if backtrack(i+1,j,cnt) or backtrack(i,j+1,cnt) or backtrack(i-1,j,cnt) or backtrack(i,j-1,cnt):
                return True
            board[i][j]=temp   
            return False

        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    if backtrack(i,j,0):
                        return True
                
        return False