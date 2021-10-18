class Solution {
public:
    int largestUniqueNumber(vector<int>& nums) {
       
    
        int hash[1001]={0};
        for(int i=0;i<nums.size();i++)
            hash[nums[i]]++;
        
        int max1=-1;
     
        for (int i=1000;i>=0;i--) {
            if(hash[i]!=0)
            //cout<<hash[i]<<endl;
            if(hash[i]==1){
                max1=i;
            break;}
        }
        return max1;
         
    }
};