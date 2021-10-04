class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        
        vector<vector<int>> k={{}};
        
        for(auto &num:nums)
        {
            int n=k.size();
            for(int i=0;i<n;i++)
            {
                k.push_back(k[i]);
                k.back().push_back(num);
            }
        }
        
        return k;
    }
};