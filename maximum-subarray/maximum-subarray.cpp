class Solution {
public:
    //use kadaane's algo
    int maxSubArray(vector<int>& nums) {
             int sum=nums[0],maxsum=nums[0];
              
        for(int i=1;i<nums.size();i++)
        {
           int n=nums[i];
            sum=max(n,n+sum);
            maxsum=max(maxsum,sum);
        }
        
        return maxsum;
    }
};