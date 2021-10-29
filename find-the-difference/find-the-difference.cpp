class Solution {
public:
    char findTheDifference(string s, string t) {
       
       int hash[26]={0};
        int hash1[26]={0};
        for(int i=0;i<s.size();i++)
            hash[int(s[i])-'a']++;
         for(int i=0;i<t.size();i++)
            hash1[int(t[i])-'a']++;
        
        char ans;
        for(int i=0;i<26;i++)
        {
            if(hash1[i]!=hash[i])
            {
                char temp=i+97;
                ans=(char)temp;
            }
        }
        
        return ans;
    }
};