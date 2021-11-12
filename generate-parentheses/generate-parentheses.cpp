class Solution {
public:
    vector<string> res;
    void generate(int n,int i,string s)
    {
       if(s.size()>2*n)
           return;
        if(i<0)
            return;
        
        if(2*n==s.size() && i==0)
        {
           res.push_back(s);
        }
        
        
        generate(n,i+1,s+'(');
        
        generate(n,i-1,s+')');
        
    }
    vector<string> generateParenthesis(int n) {
        string s;
        generate(n,0,s);
        return res;
    }
};