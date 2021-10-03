class Solution {
public:
    int distributeCandies(vector<int>& c) {
        
        unordered_map<int,int> h;
        for(int i=0;i<c.size();i++)
        {
            h[c[i]]++;
        }
        
        int k=(c.size())/2;
        
        if(k>h.size())
            return h.size();
        
        return k;
    }
};