class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        int p=-1,f=0;
        int ans=0;
        
        for(int i=0;i<seats.size();i++)
        {
            if(seats[i]==1)
                p=i;
            else
            {
                while(f<seats.size() && seats[f]==0 || f<i)
                    f++;
                
                int l=p==-1?seats.size():i-p;
                int r=f==seats.size()?seats.size():f-i;
                ans=max(ans,min(l,r));
            }
        }
        
        return ans;
    }
};