class Solution {
public:
    string reverseWords(string s) {
        
        int cnt=0;
        vector<string> k; string f;
        for(int i=0;i<s.size();i++)
        {
            
            if(s[i]!=' ')
            {
                f+=s[i];
            }
            else 
            {
                if(f.size()!=0){
                k.push_back(f);
                f.clear();
                }
            }
        }
        if(f.size()!=0)
        k.push_back(f);
        s.clear();
        for(int i=k.size()-1;i>0;i--)
        {
            s+=k[i];
            s+=' ';
        }
        s+=k[0];
        
        return s;
        
    }
};