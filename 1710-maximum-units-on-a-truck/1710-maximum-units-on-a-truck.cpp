class Solution {
public:
    static bool comp(vector<int> &a,vector<int> &b)
    {
        return a[1]>b[1];
    }
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(),boxTypes.end(),comp);
        
        //int cnt=0;
        int ans=0;
       
        for(auto b:boxTypes)
        {
            int cnt;
            cnt=min(truckSize,b[0]);
            ans+=cnt*b[1];
            truckSize-=cnt;
            if(truckSize==0)
                break;
        }
        
        return ans;
    }
};