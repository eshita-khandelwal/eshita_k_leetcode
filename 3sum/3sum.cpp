class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> k;
        if(nums.size()<3)
            return k;
      
        sort(nums.begin(),nums.end());
        
        for(int i=0; i<nums.size()-2;i++)
        {
            int a=nums[i];
            if(i>0)
            {
                if(nums[i]==nums[i-1])
                    continue;
            }
            
                int p=i+1;
                int q=nums.size()-1;
               while(p<q)
               {
                   if(nums[p]+nums[q]+a==0)
                   {
                       k.push_back({nums[p],nums[q],a});
                       p++;
                       while(nums[p]==nums[p-1] && p<q)
                       {
                           p++;
                       }
                   }
                   else if(nums[p]+nums[q]+a>0)
                   {
                       q--;
                   }
                     else if(nums[p]+nums[q]+a < 0)
                         p++;
               }
        }
        
        return k;
    }
};