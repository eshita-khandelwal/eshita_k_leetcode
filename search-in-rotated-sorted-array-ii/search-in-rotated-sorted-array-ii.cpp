class Solution {
public:
    bool search(vector<int>& nums, int target) {
        
        int start=0;
        int end=nums.size()-1;
        
        while(start<=end)
        {
            int mid=start+(end-start)/2;
            if(nums[mid]==target)
                return true;
            else if(nums[mid]>nums[start])
            {
                if(nums[mid]>target && nums[start]<=target)
                    end=mid-1;
                else
                    start=mid+1;
            }
            else if(nums[mid]<nums[start])
            {
                if(target>nums[mid] && target<=nums[end])
                   start=mid+1;
                else
                   end=mid-1; 
            }
            else
                start+=1;
        }
        
        
        return false;
    }
};