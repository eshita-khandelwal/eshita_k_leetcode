class Solution {
public:
    //no dp required use greedy 
    int shortestWay(string s, string t) {
        
        int i=0;int j=0;
        int res=0;
        while(res<=j && j<t.size())
        {
           while(i<s.size() && s[i]!=t[j])i++;
            if(i==s.size())
                i=0,res++;
            else{i++;j++;}
        }
        if(res<=j)
            return res+1;
        return -1;
    }
};