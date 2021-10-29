class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        
      
        int max1=0;
        int min1=0;
        int res=0;
        for(int i=0;i<nums.size();i++)
        {
           max1=max(0,max1+nums[i]);
            min1=min(min1+nums[i],0);
        res=max({res,max1,abs(min1)});
        }
        
        return res;
    }
};