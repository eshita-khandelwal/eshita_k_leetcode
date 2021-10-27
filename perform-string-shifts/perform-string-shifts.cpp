class Solution {
public:
    string stringShift(string s, vector<vector<int>>& shift) {
        if(s.size()==1)
            return s;
        
        for(int i=0;i<shift.size();i++)
        {
            if(shift[i][0]==0)
            {
                string s1,s2;
                if(shift[i][1]>s.size())
                    shift[i][1]=(shift[i][1])%s.size();
                for(int j=0;j<shift[i][1];j++)
                {
                    s1+=s[j];
                }
                for(int j=shift[i][1];j<s.size();j++)
                    s2+=s[j];
                
               // reverse(s1.begin(),s1.end());
                for(int j=0;j<s1.size();j++)
                {
                    s2+=s1[j];
                }
                
                s=s2;
                // s1.erase(0);
                // s2.erase(0);
                
               // cout<<"left   "<<s<<endl;
            }
            else
            {
                 string s1,s2;
                if(shift[i][1]>s.size())
                    shift[i][1]=(shift[i][1])%s.size();
                for(int j=s.size()-shift[i][1];j<s.size();j++)
                    s1+=s[j];
                for(int j=0;j<s.size()-shift[i][1];j++)
                    s2+=s[j];
                s1+=s2;
                
                s=s1;
               // cout<<"right   "<<s<<endl;
            }
        }
        
        return s;
    }
};