class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[-1,0],[1,0],[0,-1]]
        q = deque()
        fresh=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append([i,j])
        time = 0
        while q and fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    row = r+dr
                    col = c+dc
                    if (row<0 or row==len(grid)) or col<0 or col==len(grid[0]) or grid[row][col]!=1:
                        continue
                    grid[r+dr][c+dc]=2
                    fresh-=1
                    q.append([row,col])
            time+=1
        
        return time if fresh==0 else -1

