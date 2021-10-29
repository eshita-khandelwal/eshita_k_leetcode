class Solution {
public:
    //https://www.youtube.com/watch?v=os4B7MlHAbs
    int maxSubarraySumCircular(vector<int>& nums) {
        
        int max_sum=INT_MIN;
        int min_sum=INT_MAX;
        int sum1=0,sum2=0;
        int t=0;
        for(int i=0;i<nums.size();i++)
        {
            t+=nums[i];
            sum1=max(nums[i],sum1+nums[i]);
            sum2=min(nums[i],sum2+nums[i]);
            
            max_sum=max(sum1,max_sum);
            min_sum=min(sum2,min_sum);
            
        }
        
        if(max_sum>0)
            return max(max_sum,t-min_sum);
        
        return max_sum;
    }
};