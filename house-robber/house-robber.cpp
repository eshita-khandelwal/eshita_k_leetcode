class Solution {
public:
    int rob(vector<int>& nums) {
    
        int max_sum=INT_MIN,sum1=0,sum2=0;
        int dp[101]={0};
        dp[0]=0;
        dp[1]=nums[0];
        //dp[2]=nums[2];
        for(int i=2;i<=nums.size();i++)
        {
           dp[i]=max(dp[i-2]+nums[i-1],dp[i-1]);
        }
        return dp[nums.size()];
        
    }
};