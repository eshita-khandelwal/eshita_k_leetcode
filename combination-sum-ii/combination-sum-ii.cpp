class Solution {
public:
    vector<vector<int>> f;
    vector<int> x;
    int counter[51]={0};
    void combination(vector<int>& candidates, int target,int sum,int in)
    {
        if(sum==target)
        {
            // if(find(f.begin(),f.end(),x)!=f.end())
            //     return;
            f.push_back(x);
            return;
        }
        if(sum>target)
            return;
        
        for(int i=in;i<candidates.size();i++)
        {
            if(i&&candidates[i]==candidates[i-1]&&i>in)continue; // all combinations with first number will be made but then no cominations will be made with the second same number and so on. it is genius to think of *****i>in****
            sum=sum+candidates[i];
            x.push_back(candidates[i]);
            counter[candidates[i]]--;
            combination(candidates,target,sum,i+1);
            x.pop_back();
            counter[candidates[i]]++;
            sum=sum-candidates[i];
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
       int sum=0;
       int index=0;
        for(int i=0;i<candidates.size();i++)
            counter[candidates[i]]++;
        sort(candidates.begin(),candidates.end());
        combination(candidates,target,sum,index);
         return f;
        
    }
};