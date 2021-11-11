class Solution {
public:
    static bool comp(pair<int,int> &a,pair<int,int> &b)
    {
        return a.second>b.second;
    }
    int findShortestSubArray(vector<int>& nums) {
        
        unordered_map<int,int> map;
        for(int i=0;i<nums.size();i++)
            map[nums[i]]++;
        
        vector<int> l;
        vector<pair<int,int>> count;
        for(auto x:map)
            count.push_back(x);
        
        sort(count.begin(),count.end(),comp);
        
        for(int i=0;i<count.size();i++)
        {
            if(count[0].second==count[i].second)
                l.push_back(count[i].first);
            else
                break;
        }
        
        int i=0;
        int min1=INT_MAX;
        while(i<l.size())
        {
            
            int a,b;
            //cout<<l[i]<<"  ";
            for(int j=0;j<nums.size();j++)
            {
                if(nums[j]==l[i])
                {
                    a=j;break;
                }
            }
            
            for(int j=nums.size()-1;j>=0;j--)
            {
                if(nums[j]==l[i])
                {
                    b=j;break;
                }
            }
          //  cout<<min1<<" before";
             min1=min(min1,b-a+1);
           // cout<<min1<<endl;
            i++;
        }
        
        return min1;
        
    }
};