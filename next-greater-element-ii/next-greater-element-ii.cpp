class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> x;
        for(int i=0;i<nums.size();i++)
        {
            
            int j=i+1;
            if(j==nums.size())
                j=0;
            while(true)
            {
                if(j==i){
                    x.push_back(-1);
                    break;
                }
                if(nums[j]>nums[i]){
                    x.push_back(nums[j]);break;}
                j++;
                if(j==nums.size())
                    j=0;
            }
        }
        
        return x;
    }
};