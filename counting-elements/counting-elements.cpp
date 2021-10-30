class Solution {
public:
    int countElements(vector<int>& arr) {
        int hash[1001]={0};
        for(int i=0;i<arr.size();i++)
        {
            hash[arr[i]]++;
        }
        int cnt=0;
        for(int i=0;i<1000;i++)
        {
            if(hash[i+1]>0 && hash[i]>0)
            {
                cnt+=hash[i];
            }
        }
            
      return cnt;
    
    }
};