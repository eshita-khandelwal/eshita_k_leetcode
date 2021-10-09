class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        unordered_map<int,int> m;
        for(int i=0;i<nums.size();i++)
            m[nums[i]]++;
        int max1=INT_MIN;
        for(int i=0;i<m.size();i++)
        {
            if(m[i]>max1)
            {
                max1=m[i];
            }
        }
        vector<int> l;
        for(int i=0;i<m.size();i++)
        {
            if(m[i]==max1)
            l.push_back(i);
        }
        
        int min1=INT_MAX;
        int x=0;
        int f=0;
        int count=0;
        int i=0;
        int count_f=0;
        while(i<nums.size())
        {
            if(f==0 && nums[i]==l[x])
            {
                f=1;
                count++;
                count_f++;
                
            }
            else if(f==1)
            {
                //cout<<count<<"   "<<l[x]<<"   "<<count_f<<"     "<<nums[i]<<endl;
                if(nums[i]!=l[x] || nums[i]==l[x])
                count++;
                if(nums[i]==l[x]){
                    
                    count_f++;
                }
            }
            
            if(count_f==max1)
            {
                //cout<<count<<"    "<<l[x]<<endl;
                if(min1>count)
                {
                    min1=count; 
                }
                //cout<<l[x]<<endl;
                 x++;
                    count=0;
                    count_f=0;
                    f=0;
                
                    if(x==l.size())
                        break;
                i=0;
                continue;
            }
            i++;
            if(i==nums.size())
                    i=0;
        }
        
        return min1;
    }
};