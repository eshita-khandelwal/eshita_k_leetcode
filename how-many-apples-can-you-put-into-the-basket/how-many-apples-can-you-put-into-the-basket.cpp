class Solution {
public:
    int maxNumberOfApples(vector<int>& weight) {
        
        int sum=0;
        int cnt=0;
        sort(weight.begin(),weight.end());
        for(int i=0;i<weight.size();i++)
        {
            sum+=weight[i];
            cnt++;
            if(sum>5000)
            {
                cnt--;
                break;
            }
            if(sum==5000)
                break;
                //return cnt;
                
        }
        
    return cnt;
    }
};