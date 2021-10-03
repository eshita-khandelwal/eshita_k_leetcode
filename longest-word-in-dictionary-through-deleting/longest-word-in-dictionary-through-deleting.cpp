class Solution {
public:
    int check(string a,string b)
    {
        int j=0;
        for(int i=0;i<b.size() && j<a.size();i++)
        {
            if(a[j]==b[i])
                j++;
        }
        return (j==a.size());
    }
    static bool comp(string a,string b)
    {
        if(a.size()==b.size())
            return a<b;
        
        return b.size()>a.size();
    }
    string findLongestWord(string s, vector<string>& d) {
        int max1=0;
        int maxind=-1;
        sort(d.begin(),d.end(), comp);
        for(int i=0;i<d.size();i++)
        {
            int k=check(d[i],s);
            if(k==1)
            {
                if(max1<d[i].size())
               {
                 max1=d[i].size();
                 maxind=i;
                   
               }
            }
        }
       // int c="abe"<"abc";
       // cout<<c;
        if(maxind==-1)
            return "";
        return d[maxind];
        
    }
};