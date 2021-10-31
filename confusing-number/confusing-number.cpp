class Solution {
public:
    bool confusingNumber(int n) {
      
    
        int a[10]={0,1,2,3,4,5,9,7,8,6};
        int i=n;
        int hash[10]={0};
        int reverseno=0;int x=0;
        while(n>0)
        {
            hash[n%10]++;
            reverseno+=a[(n%10)]*pow(10,x++);
            if(n%10==2|| n%10==3 || n%10==4 || n%10==5
              || n%10==7)
                return false;
            n=n/10;
        }
        
      string m=to_string(reverseno);
        string p=to_string(i);
        reverse(m.begin(),m.end());
        cout<<m<<"   "<<p<<endl;
        
        if(m==p)
            return false;
        return true;
    }
};