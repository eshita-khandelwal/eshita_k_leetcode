class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        unordered_map<string,vector<string>> map;
        for(int i=0;i<strs.size();i++)
        {
            string s;
            s=strs[i];
            sort(s.begin(),s.end());
            map[s].push_back(strs[i]);
            
        }
        
        for(auto x:map)
            result.push_back(x.second);
        
        return result;
    }
};