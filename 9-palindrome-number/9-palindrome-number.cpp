class Solution {
public:
    bool isPalindrome(int x) {
        string a= to_string(x);
        int c =0;
        while(c<a.size())
        {
            if(a[c]!=a[a.size()-c-1])
            return false;
            c++;
        }
        return true;
    }
};