class Solution {
public:
    int twoSumLessThanK(vector<int>& nums, int k) {
        
       sort(nums.begin(),nums.end());
        int max1=-1;
        int i=0;int j=nums.size()-1;
        while(i<j)
        {
            if(nums[i]+nums[j]<k)
            {
                if(nums[i]+nums[j]>max1)
                    max1=nums[i]+nums[j];
               i++;
            }
            else if(nums[i]+nums[j]>=k)
                j--;
        }
        
        return max1;
    }
};