class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> map;
        vector<int> result;
        for(int i=0;i<nums.size();i++)
        {
            
            if(map.find(nums[i])!=map.end())
            {
                result.push_back(map[nums[i]]);
                result.push_back(i);
            }
            map[target-nums[i]]=i;
        }
        
        return result;
    }
};