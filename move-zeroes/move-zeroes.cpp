class Solution {
public:
    void moveZeroes(vector<int>& nums) {
       
        int j=0;int c=0;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]!=0)
            nums[j++]=nums[i];
            else
                c++;
                
        }
        for(int i=j;i<nums.size();i++)
            nums[i]=0;
        
        //return nums;
    }
};