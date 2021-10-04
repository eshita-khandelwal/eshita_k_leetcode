class Solution {
public:
    vector<vector<int>> m;
    vector<int> f;
    
    void combination(vector<int>& candidates, int target,int sum,int index)
    {
        if(target==sum)
        {
            m.push_back(f);
            return;
        }
        if(target<sum)
            return;
        
        for(int i=index;i<candidates.size();i++)
        {
            sum=sum+candidates[i];
            f.push_back(candidates[i]);
            combination(candidates,target,sum,i);
            //cout<<candidates[i]<<endl;
            sum-=candidates[i];
            f.pop_back();
        }
        
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        
        int sum=0;
        combination(candidates,target,sum,0);
        return m;
    }
};