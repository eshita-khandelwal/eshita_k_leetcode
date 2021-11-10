class Solution {
public:
    bool isvowel(char a)
    {
        if(a=='a' || a=='e' || a=='o' || a=='i' || a=='u')
            return true;
        return false;
    }
    string removeVowels(string s) {
        string result;
        for(int i=0;i<s.size();i++)
        {
            if(isvowel(s[i]))
                continue;
            result+=s[i];
        }
        
        return result;
    }
};