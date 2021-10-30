class Solution {
public:
    //https://www.youtube.com/watch?v=1WGtcErMPrQ
    int repeatedStringMatch(string a, string b) {
        
        int lena=a.size();
        int lenb=b.size();
        
        int repeat=(b.size()/a.size())+2;
        int cnt=1;
        string x=a;
        for(int i=0;i<repeat;i++)
        {
            if(x.find(b)!=string::npos)
                return cnt;
            else
            {
                x+=a;
                cnt++;
            }
        }
        
        return -1;
    }
};