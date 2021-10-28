class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        
        int inc=0;
        int exec=0;
        int count[20001]={0};
        for(int i=0;i<nums.size();i++)
            count[nums[i]]++;
        for(int i=0;i<20001;i++)
        {
            int in=exec+count[i]*i;
            int ex=max(exec,inc);
            inc=in;
            exec=ex;
        }
        
        return max(inc,exec);
    }
};