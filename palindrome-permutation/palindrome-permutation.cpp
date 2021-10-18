class Solution {
public:
    bool canPermutePalindrome(string s) {
        
        int hash[26]={0};
        for(int i=0;i<s.size();i++)
            hash[int(s[i])-97]++;
    
         int cnt=0;
        for(int i=0;i<26;i++)
        {
            if(hash[i]%2==0)
                continue;
            else
                cnt++;
        }
        if(s.size()%2==0 && cnt>0)
            return false;
        else if(s.size()%2==0 && cnt==0)
            return true;
        else if(s.size()%2==1 && cnt==1)
            return true;
        else if(s.size()%2==1 && cnt>1)
            return false;
        
        return true;
    }
};