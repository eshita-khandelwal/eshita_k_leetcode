class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        
        priority_queue<int> elements;
        for(int i=0;i<nums.size();i++)
            elements.push(nums[i]);
        
        for(int i=0;i<k-1;i++)
            elements.pop();
        
        return elements.top();
    }
};