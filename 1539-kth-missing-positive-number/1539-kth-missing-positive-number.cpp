class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        
        int hash[1001]={0};
        
        for(int i=0;i<arr.size();i++)
        {
            hash[arr[i]]=1;
        }
        
        int i;
        for(i=1;i<1001;i++)
        {
            if(hash[i]==0)
                k--;
            if(k==0)
                break;
        }
        if(k!=0)
        {
            i=1000+k;
        }
        return i;
    }
};