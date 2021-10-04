class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        sort(arr.begin(),arr.end());
        int n=arr.size();
        if(n<3)
            return true;
        vector<int> dp(n,0);
         dp[0]=1;
       dp[1]=1;
       
        if(arr[2]-arr[0]==2*(arr[2]-arr[1])){
           // cout<<"hi";
            dp[2]=1;
        }
       
        for(int i=3;i<arr.size();i++)
        {
           if(arr[i]-arr[i-2]==2*(arr[i]-arr[i-1]))
               dp[i]=dp[i-1] && 1;
            else
                return false;
        }
        
        return dp[n-1];
    }
};