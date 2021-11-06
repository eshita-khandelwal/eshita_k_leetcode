class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        vector<int>x;
        sort(nums.begin(),nums.end());
        int i=0;
        while(i<nums.size())
        {
            int j=i+1;
            
            if(j<nums.size() && i<nums.size() && nums[i]==nums[j])
            {
                while(j<nums.size() && nums[i]==nums[j])
                    j++;
            }
            else
                x.push_back(nums[i]);
            
            i=j;
        }
        
        return x;
    }
};