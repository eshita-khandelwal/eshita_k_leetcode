class Solution {
public:
    vector<vector<int>> highFive(vector<vector<int>>& items) {
        unordered_map<int,vector<int>> x;
        for(int i=0;i<items.size();i++)
        {
            x[items[i][0]].push_back(items[i][1]);
        }
        for(int i=0;i<x.size();i++)
        {
            if(x[i].size()==0)
                continue;
              sort(x[i].begin(),x[i].end(),greater<int>());
        }
        vector<vector<int>> y;
        for(int i=1;i<x.size();i++)
        {
           int sum=0;int k=0;
            for(int j=0;j<x[i].size();j++)
            {
                sum+=x[i][j];
                k++;
                if(k==5)
                    break;
            }
            if(sum!=0)
            y.push_back({i,sum/5});
        }
        
        return y;
    }
};