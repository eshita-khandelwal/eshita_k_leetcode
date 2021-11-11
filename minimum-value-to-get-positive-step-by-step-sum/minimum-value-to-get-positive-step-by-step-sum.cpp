class Solution {
public:
    int minStartValue(vector<int>& nums) {
        
        for(int i=1;i<=100000000;i++)
        {
            int j=0;int sum=i;
            for(j=0;j<nums.size();j++)
            {
                sum+=nums[j];
                if(sum<1)
                    break;
            }
            if(j==nums.size())
                return i;
        }
        
        return -1;
    }
};