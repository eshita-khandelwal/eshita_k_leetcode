class Solution {
public:
    // keep an array seen to maintain the cells visited and each cell should be counted only once.
    int visited[50][50];
    
    int  area(vector<vector<int>> &grid,int r,int c)
    {
       
         if(r<0 || c<0 || r>=grid.size() || c>=grid[0].size() || visited[r][c]==1 ||
          grid[r][c]==0)
            return 0;
        visited[r][c]=1;
        return (1+area(grid,r-1,c)+area(grid,r,c-1)+area(grid,r+1,c)+area(grid,r,c+1));
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
       
        for(int i=0;i<50;i++)
        {
            for(int j=0;j<50;j++)
            {
                visited[i][j]=0;
            }
        }
        int ans=INT_MIN;
        for(int i=0;i<grid.size();i++)
        {
            for(int j=0;j<grid[0].size();j++)
            {
               ans=max(ans,area(grid,i,j)); 
            }
        }
        
        return ans;
        
    }
};