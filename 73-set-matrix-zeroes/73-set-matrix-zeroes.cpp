class Solution {
public:
    
    
    void setZeroes(vector<vector<int>>& matrix) {
        
        
        set<int> r,c;
        set<int> :: iterator itr;
        
        for(int i=0;i<matrix.size();i++)
        {
        
            for(int j=0;j<matrix[0].size();j++)
            {
               
                   if(matrix[i][j]==0)
                   {
                       r.insert(i);
                       c.insert(j);
                   }
            }
            
        }
        
        for(itr=r.begin(); itr!=r.end();itr++)
        {
            for(int j=0;j<matrix[0].size();j++)
            {
                matrix[*itr][j]=0;
            }
        }
        
        for(itr=c.begin();itr!=c.end();itr++)
        {
            for(int j=0;j<matrix.size();j++)
            {
                matrix[j][*itr]=0;
            }
        }
    }
};