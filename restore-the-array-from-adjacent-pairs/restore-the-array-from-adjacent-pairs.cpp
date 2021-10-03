class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& a) {
        unordered_map<int,vector<int>> k;
        for(int i=0;i<a.size();i++)
        {
            k[a[i][0]].push_back(a[i][1]);
            k[a[i][1]].push_back(a[i][0]);
        }
        vector<int> res;
        
        for(auto &p : k)
        {
            if(p.second.size()==1)
            {
                res.push_back(p.first);
                res.push_back(p.second[0]);
                break;
            }
        }
        
        while(res.size()<a.size()+1)
        {
            int element_next=res.back();
            int prev=res[res.size()-2];
            auto &next=k[element_next];
            
            if(next[0]!=prev)
            {
                res.push_back(next[0]);
            }
            else
                res.push_back(next[1]);
        }
        return res;
    }
};