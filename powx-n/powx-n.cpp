class Solution {
public:
    double myPow(double x, int n) {
         double ans=1;
        long long N=n;
        cout<<x;
        if(n==0)
            return 1;
        if(n<0)
        {
            ans=pow(1/x,-N/2);
              if(n%2==0)
                  ans=ans*ans;
            else
                ans=ans*ans*1/x;
        }
        else
        {
            ans=pow(x,N/2);
              if(n%2==0)
                  ans=ans*ans;
            else
                ans=ans*ans*x;
        }
        
        return ans;
        
    }
};