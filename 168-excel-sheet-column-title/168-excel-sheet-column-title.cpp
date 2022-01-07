class Solution {
public:
    string convertToTitle(int n) {
       
        string s1;
        char temp;
        
        while(n)
        {
            n=n-1;
            temp='A' + n%26;
            s1=temp+s1;
            n=n/26;
        }
        
        return s1;
    }
};