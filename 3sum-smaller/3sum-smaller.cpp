class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {
       int cnt=0;
       
        if(nums.size()<3)
            return 0;
         sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size()-2;i++)
        {
            // if(i>0 && nums[i]==nums[i+1])
            //     continue;
            int p=i+1;
            int q=nums.size()-1;
            int t=target-nums[i];
            while(p<q)
            {
                if(nums[p] + nums[q] < t){
                    cnt+=q-p;
                    p++;
                    // while(p<q && nums[p]==nums[p-1])p++;
                }
                
                else 
                    q--;
                
            }
            
        }
        
        return cnt;
    }
};