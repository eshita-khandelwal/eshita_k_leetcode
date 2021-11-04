class Solution {
public:
    static bool comp(pair<int,int> &a,pair<int,int> &b)
    {
        return a.first<b.first;
    }
    int smallestCommonElement(vector<vector<int>>& mat) {
        unordered_map<int,int> x;
        
        for(int i=0;i<mat.size();i++)
        {
            for(int j=0;j<mat[0].size();j++)
            {
                x[mat[i][j]]++;
            }
        }
        
        vector<pair<int,int>> y;
        
        for(auto m:x)
            y.push_back(m);
        
        sort(y.begin(),y.end(),comp);
        for(int i=0;i<y.size();i++)
        {
            if(y[i].second==mat.size())
                return y[i].first;
        }
        return -1;
    }
};