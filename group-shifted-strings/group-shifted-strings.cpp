class Solution {
public:
 
    vector<vector<string>> groupStrings(vector<string>& s) {
        
        int cnt=0;
        //sort(s.begin(),s.end(),comp);
        map<vector<int>,vector<string>> mp;
        for(int i=0;i<s.size();i++)
        {
            vector<int> temp;
            for(int j=1;j<s[i].size();j++)
            {
                temp.push_back((26+s[i][j]-s[i][j-1])%26);
            }
           
            mp[temp].push_back(s[i]);
        }
        
        vector<vector<string>> k;
        for(auto x:mp)
        {
            vector<string> g;
            g=x.second;
            k.push_back(g);
        }
        //sort(k.begin(),k.end(),comp);
       return k; 
    }
};