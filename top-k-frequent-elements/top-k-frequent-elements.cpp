class Solution {
public:
    static bool comp(pair<int,int> &a,pair<int,int> &b)
    {
        return a.second>b.second;
    }
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> count;
        for(int i=0;i<nums.size();i++)
            count[nums[i]]++;
        vector<pair<int,int>> sort_map;
        
        for(auto x:count)
            sort_map.push_back(x);
        
        sort(sort_map.begin(),sort_map.end(),comp);
        
        vector<int> x;
    for(int i=0;i<min(k,(int)sort_map.size());i++)
    {
        x.push_back(sort_map[i].first);
    }
        
        return x;
    }
};