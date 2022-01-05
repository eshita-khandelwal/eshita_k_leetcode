class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
       
        map<int,int> m;
        for(int i=0;i<trust.size();i++)
            m[trust[i][0]]++;
        
        
        if(m.size()==n)
            return -1;
        
        int i;
        for(i=1;i<=n;i++)
        {
           if(m.find(i)==m.end())
               break;
        }
        int cnt=0;
        for(int j=0;j<trust.size();j++)
        {
            if(trust[j][1]==i)
                cnt++;
        }
        if(cnt==n-1)
        return i;
        return -1;
    }
};