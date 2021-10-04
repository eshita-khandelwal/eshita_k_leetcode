class Solution {
public:
    static bool comp(string &a,string &b)
    {
        return a+b>b+a;
    }
    string largestNumber(vector<int>& nums) {
        vector<string> k;
        
        for(int i=0;i<nums.size();i++)
        {
            k.push_back(to_string(nums[i]));
        }
        
        sort(k.begin(),k.end(),comp);
        string res;
        for(auto &s:k)
        {
            res+=s;
        }
        
        while(res[0]=='0' && res.size()>1)
            res.erase(0,1);
        
        return res;
    }
};