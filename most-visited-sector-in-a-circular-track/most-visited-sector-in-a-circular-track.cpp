class Solution {
public:
    vector<int> mostVisited(int n, vector<int>& rounds) {
        
        int visited[101]={0};
        for(int i=0;i<rounds.size()-1;i++)
        {
            
            int m=rounds[i];
            
            while(true)
            {
                visited[m]++;
                if(m==rounds[i+1])
                {
                    if(i+1!=rounds.size()-1)
                    visited[m]--;
                    break;
                }
                m++;
                if(m==n+1)
                    m=1;
                
            }
            
            
        }
        
        vector<int> maxa;
        int max1=INT_MIN;
        for(int i=1;i<n+1;i++)
        {
           // cout<<visited[i]<<endl;
            if(max1<visited[i])
                max1=visited[i];
        }
        
        for(int i=1;i<n+1;i++)
        {
            if(visited[i]==max1)
                maxa.push_back(i);
        }
        
        return maxa;
    }
};