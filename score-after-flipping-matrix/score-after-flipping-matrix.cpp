class Solution {
public:
    int matrixScore(vector<vector<int>>& A) {
        
       int rows=A.size();
        int col=A[0].size();
        int res=(1<<col-1)*rows;
        for(int j=1;j<col;j++)
        {
            int cur=0;
            for(int i=0;i<rows;i++)
            {
                if(A[i][0]==A[i][j])
                    cur++;
            }
            res+=max(cur,rows-cur)*(1<<col-1-j);
            
        }
        
        return res;
    }
};