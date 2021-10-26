class Solution {
public:
    bool areSentencesSimilar(vector<string>& s1, vector<string>& s2, vector<vector<string>>& similarPairs) {
        if(s1.size()!=s2.size())
            return false;
        
        if(similarPairs.size()==0)
        {
            for(int i=0;i<s1.size();i++)
            {
                if(s1[i]==s2[i])
                {}
                else
                    return false;
            }
            return true;
        }
        
        
        else
        {
            for(int i=0;i<s1.size();i++)
            {
                int f=0;
                for(int j=0;j<similarPairs.size();j++)
                {
                    if(s1[i]!=s2[i])
                    {
                        if(similarPairs[j][0]==s1[i] && similarPairs[j][1]==s2[i]){f=0;break;}
                        else if(similarPairs[j][1]==s1[i] && similarPairs[j][0]==s2[i]){f=0;break;}
                        else
                            f=1;
                    }
                }
                if(f==1)
                    return false;
                
            }
            
            return true;
        }
      
        return true;
    }
};